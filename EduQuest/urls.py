"""
URL configuration for EduQuest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from app.views import *

urlpatterns = [
   
    path('app/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('app/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('app/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('app/', include('app.urls')),
  
    path("profile/", user_profile, name='profile'),  # Profile sayfası için yol ekle
    path("", launchpage, name='launch'),  # Launch sayfası için yol
    path("editorcontrol", editorcontrol, name='editorcontrol'),  # Launch sayfası için yol
    path("register/", register, name='register'),  # Kayıt sayfası için yol ekle
    path("login/", user_login, name='login'),  # Giriş sayfası için yol ekle # Google login için allauth URL'lerini dahil et
    path('profile/', user_profile, name='profile'),  # Profil sayfası URL'si
    path('logout/', user_logout, name='logout'),  # Çıkış işlemi URL'si
]
