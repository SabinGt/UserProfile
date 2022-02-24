from django.shortcuts import render, redirect
from .models import CustomUser
import requests


# Create your views here.
def fillForm(request):
    return render(request,'fillForm.html')

#function for home page
def home(request):
    if request.user.is_authenticated:
        if not request.user.profile_completed:
            return redirect('fillForm')
        return redirect('profile')
    else:
        return redirect('account_login')

def my_profile(request,*args,**kwargs):
    current_user=  request.user
    context = {}
    context['user'] = current_user
    return render(request,'profile.html',context)    




    
