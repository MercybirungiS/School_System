from django.db import models
from django.db.models.fields import files


# Create your models here.

class Events(models.Model):
    event_name=models.CharField(max_length=12,default='DEFAULT VALUE', blank=True, null=True)
    event_description=models.TextField(blank=True, null=True)
    event_duration=models.TimeField(blank=True, null=True)
    event_agenda=models.CharField(max_length=200,blank=True, null=True)
    event_venue=models.CharField(max_length=15,blank=True, null=True)
    event_organiser=models.CharField(max_length=12,blank=True, null=True)
    event_link=models.CharField(max_length=12,blank=True, null=True)
   