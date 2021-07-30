from django.db import models


# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    admission_date=models.DateField()
    medical_form=models.FileField()
    laptop_serial_number=models.CharField(max_length=4)
    natioinal_id=models.CharField(max_length=20)
    nationality_choice=(
        ('1','Rwandan'),
        ('2','Kenyan'),
        ('3','Ugandan'),
        ('4','SouthSudanes'),
        ('5','Sudanes')
    )
    nationality=models.CharField(max_length=15,choices=nationality_choice)
    gender_choice=(
        ('1','Female'),
        ('2','Male'),
        ('3','none')
    )
    gender=models.CharField(max_length=8,choices=gender_choice)
    email_address=models.EmailField()
    district=models.CharField(max_length=12)
    course_name=models.CharField(max_length=18)
    
 
    

