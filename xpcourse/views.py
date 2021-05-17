from django.http.response import HttpResponse
from users.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import logout, login as auth_login
from django.contrib.auth.hashers import check_password

def index(request):
    return render(request, 'index.html', {})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        
        if check_password(password, user.password):
            if user.is_active:
                auth_login(request, user)
                return redirect('index')
    else:
        return render(request, 'index.html', {})

def signUp(request):
    if request.method == 'POST':
        user = User.objects.create(
            username=request.POST['username'],
            email=request.POST['email']
        )
        user.set_password(request.POST['password'])
        user.save()
        auth_login(request, user)
        return redirect('index')
    return render(request, 'auth/signUp.html', {})

def signOut(request):
    logout(request)
    return redirect('index')