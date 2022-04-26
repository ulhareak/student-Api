from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, default='teacher')

    def __str__(self):
        return f'{self.role}'


class Subject(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    standard = models.IntegerField()
#    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.f_name}'


class Result(models.Model):
    student = models.ForeignKey(Student,related_name = 'student', on_delete=models.CASCADE )
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE , related_name= 'subject')
    marks = models.IntegerField()
    exam_date = models.DateField()
