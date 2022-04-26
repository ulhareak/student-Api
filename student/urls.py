

from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("stu",views.CustomeApi)

#app_name = 'student'

urlpatterns = [
    path('student/',views.StudentView.as_view()),
    path('result/', views.ResultApiView.as_view()),
    path("" , include(router.urls))
]