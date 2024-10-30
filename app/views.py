# app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    return render(request, 'profile.html')  



def launchpage(request):
    return render(request, 'base.html')  
