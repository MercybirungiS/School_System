from django.db import models
from django.db.models.fields import files

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=12,default='DEFAULT VALUE', blank=True, null=True)
    last_name=models.CharField(max_length=12,default='DEFAULT VALUE', blank=True, null=True)
    gender_choice=(
        ('1','Female'),
        ('2','Male'),
        ('3','Binary')
    )
    gender=models.CharField(max_length=8,choices=gender_choice,default='DEFAULT VALUE', blank=True, null=True)
    age=models.PositiveSmallIntegerField(default='DEFAULT VALUE', blank=True, null=True)
    phone_number=models.CharField(max_length=10,default='DEFAULT VALUE', blank=True, null=True)
    natioinal_id=models.CharField(max_length=20,default='DEFAULT VALUE', blank=True, null=True)
    email_address=models.EmailField(default='DEFAULT VALUE', blank=True, null=True),
    contract=models.FileField(upload_to="files/",default='DEFAULT VALUE', blank=True, null=True)
    resume=models.FileField(upload_to="files/",default='DEFAULT VALUE', blank=True, null=True)
    salary=models.PositiveBigIntegerField(default='DEFAULT VALUE', blank=True, null=True)
    profile_pic=models.ImageField(upload_to="images/",default='DEFAULT VALUE', blank=True, null=True)
    syllabus=models.CharField(max_length=15,default='DEFAULT VALUE', blank=True, null=True)
    company=models.CharField(max_length=12,default='DEFAULT VALUE', blank=True, null=True)
    

