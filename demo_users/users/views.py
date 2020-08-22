from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

def CreateUser(request):
    if request.user.is_superuser:   
        name=request.username
        email=request.email
        if request.type==True:
            user=User.objects.create_superuser(name,email,'Shakugan1') 
        else:
            pass