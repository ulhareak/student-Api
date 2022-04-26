from django.shortcuts import render
# from simplejson import dumps
from . import serializers
from . import models
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import *
from rest_framework.serializers import ListSerializer
from django.core import serializers as d_ser
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import Paginator
import json
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class StudentView(ListCreateAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class ResultApiView(CreateAPIView):
    # authentication_classes = (BasicAuthentication ,)
    # permission_classes = (IsAdminUser,)
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer

class CustomePagination(PageNumberPagination):
    page_size = 2

class CustomeApi(ModelViewSet):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    pagination_class = CustomePagination

    @action(detail=False, methods=['get'])
    def total(self , request):
        date = self.request.GET.get('q', None)
        queryset = models.Result.objects.filter(exam_date=date)
        # .values(
        #     'subject').annotate(total=Count('student')) #.values('subject','total')
        print("qs",type(queryset[0].subject))
        data = serializers.TestSerializer(queryset, many=True).data #.initial_data
        paginator = PageNumberPagination()
        paginator.page_size = 2

        result_page = paginator.paginate_queryset(data, request)
        return paginator.get_paginated_response(result_page)
        #
        # print("qs", qs)
        #p = Paginator(qs , 2)
        # ser = serializers.TestSerializer(data = list(qs) , many = True )
        #queryset = self.filter_queryset(self.get_queryset())
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer =serializers.TestSerializer(queryset, many=True).data #self.get_serializer(page, many=True)
        #     #serializer = serializers.TestSerializer("json", list(queryset), many=True).initial_data
            
        #     result = self.get_paginated_response(serializer)
        #     data = result.data # pagination data
        # else:
        #     serializer = serializers.TestSerializer(queryset, many=True).data #self.get_serializer(queryset, many=True)
        #     data = serializer.data
        # # data = serializers.TestSerializer(
        # #     "json", list(qs), many=True).initial_data
        
        # # return Response(data)
        # payload = {
        #     'return_code': '0000',
        #     'return_message': 'Success',
        #     'data': data
        # }
        # return Response(data)

    @ action(detail=False, methods=['get'])
    def avg_marks(self, request):
        date=self.request.GET.get('q', None)
        qs=models.Result.objects.filter(exam_date=date).values(
            'subject').annotate(avg=Avg("marks"))
        print("qs", qs)
        # data=serializers.TestSerializer(
        #     "json", list(qs), many=True).initial_data
        data = serializers.TestSerializer(instance ={'qs' :qs})
        return Response(data)

    @ action(detail=False, methods=['get'])
    def sum_of_marks_of_subject(self, request):
        date=self.request.GET.get('q', None)
        qs=models.Result.objects.filter(exam_date=date).values(
            'subject').annotate(total=Sum('marks'))
        print("qs", qs)
        data=serializers.TestSerializer(
            "json", list(qs), many=True).initial_data
        return Response(data)
