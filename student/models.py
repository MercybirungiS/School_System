from django.db import models



# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    gender_choice=(
        ('1','Female'),
        ('2','Male'),
        ('3','Binary')
    )
    gender=models.CharField(max_length=8,choices=gender_choice)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    phone_number=models.CharField(max_length=10)
    nationality_choice=(
        ('1','Rwandan'),
        ('2','Kenyan'),
        ('3','Ugandan'),
        ('4','SouthSudanes'),
        ('5','Sudanes')
    )
    nationality=models.CharField(max_length=15,choices=nationality_choice)
    natioinal_id=models.CharField(max_length=20)
    email_address=models.EmailField()
    academic_qualification_choice=(
        ('1' ,'Bachelors'),
        ('2','Diploma'),
        ('3' ,'Certificate'),
        ('4','High School Diploma')
    )
    academic_level=models.CharField(max_length=20,choices=academic_qualification_choice)
    # admission_date=models.DateField()
    academic_documents=models.FileField()
    medical_form=models.FileField()
   
    district=models.CharField(max_length=12)
   
  
   
    
 
    

