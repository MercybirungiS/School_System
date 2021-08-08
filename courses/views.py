from django import forms
from django.shortcuts import render
from .forms import CoursesForm


# Create your views here.
def register_course (request):
    if request.method=="POST":
       form=CoursesForm(request.POST)
       if form.is_valid():
            form.save()
       else:
            print(form.errors)
    else:
        form=CoursesForm()
    return render(request,"register_course.html",{"form":form})

