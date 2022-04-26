from django.contrib import admin
from . import models 


# Register your models here.





@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id' ,"f_name","l_name",'standard') #,"subject"

@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id' ,"name")

@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id' ,"student","subject",'marks',"exam_date")

@admin.register(models.UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id' ,'user','role')

