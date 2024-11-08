# app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    return render(request, 'profile.html')  

def launchpage(request):
    return render(request, 'mainpage.html')  

def editorcontrol(request):
    return render(request, 'editorcontrol.html' )  

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('launch')  # Kayıt olduktan sonra yönlendirme
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('launch')  # Giriş yaptıktan sonra yönlendirme
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_profile(request):
    # Kullanıcının bilgilerini almak için request.user kullanabilirsiniz
    user = request.user
    return render(request, 'profile.html', {'user': user})


from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('launch')  # Çıkış yapınca yönlendirilecek yer