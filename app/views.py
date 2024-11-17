# app/views.py
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Sum, Count, Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.utils.dateparse import parse_datetime
from decimal import Decimal
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    return render(request, 'profile.html')  

def home(request):
    return JsonResponse({"message": "Welcome to EduQuest API!"})

def launchpage(request):
    return render(request, 'mainpage.html')  

def editorcontrol(request):
    return render(request, 'editorcontrol.html' )
