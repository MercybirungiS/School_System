from django import forms
from django.shortcuts import render
from.forms import EventsForm

# Create your views here.

def register_event (request):
    if request.method=="POST":
       form=EventsForm(request.POST)
       if form.is_valid():
            form.save()
       else:
            print(form.errors)
    else:
        form=EventsForm()
    return render(request,"register_event.html",{"form":form})

