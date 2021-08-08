
from django.db import models
from django.db.models.fields import files


# Create your models here.
class Courses(models.Model):
    course_name=models.CharField(max_length=12,default='DEFAULT VALUE', blank=True, null=True)
    course_code=models.CharField(max_length=12,default='DEFAULT VALUE', blank=True, null=True)
    trainer=models.CharField(max_length=12,default='DEFAULT VALUE', blank=True, null=True)
    course_description=models.CharField(max_length=12,default='DEFAULT VALUE', blank=True, null=True)
    stack=models.CharField(max_length=12,default='DEFAULT VALUE', blank=True, null=True)
    course_material=models.FileField(upload_to="files/",default='DEFAULT VALUE', blank=True, null=True)
    course_duration=models.CharField(max_length=12,default='DEFAULT VALUE', blank=True, null=True)
    
    
