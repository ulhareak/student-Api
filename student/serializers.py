


from . import models
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer



class StudentSerializer(ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id',"f_name","l_name",'standard']

class ResultSerializer(ModelSerializer):
    #total = serializers.IntegerField()
    class Meta:
        model = models.Result
        fields = ["student","subject",'marks',"exam_date",'total']
class SubjectSerializer(ModelSerializer):
    class Meta :
        model = models.Subject
        fields = ('id','name')

# class TestSerializer(serializers.Serializer):
#     subject = serializers.CharField()
#     #subject = SubjectSerializer(many = True )
#     total = serializers.IntegerField()


# class TestSerializer(serializers.ModelSerializer):
#     subject = serializers.StringRelatedField( read_only=True)
#     total = serializers.IntegerField()

#     class Meta:
#         model = models.Subject
#         fields = ['subject','total']


class TestSerializer(FlexFieldsModelSerializer):
    #subject = serializers.StringRelatedField(read_only=True)
    #total  = serializers.IntegerField()
    class Meta:
        model = models.Result
        fields = ['subject'] #, 'total']

        expandable_fields = {
            'subject': SubjectSerializer
        }
