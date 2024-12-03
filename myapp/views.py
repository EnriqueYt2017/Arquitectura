from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import *
from django.db import connection
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

# Create your views here.
def hello(request, username):
    return HttpResponse("Hello, Django! % s" % username) 

def home(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'pages/contacto.html')

def talleres(request):

    talleres = Taller.objects.all()
    context = {
        'talleres': talleres
    }
    
    return render(request, 'pages/talleres.html',context)

def servicios_apoyo(request):
    return render(request, 'pages/servicios_apoyo.html')


def login(request):
    aux = {
        'form': CustomUserLoginForm()
    }
    if request.user.is_authenticated:
        messages.info(request, 'Ya estás logeado')
        return redirect(to="home")
    
    if request.method == 'POST':
        aux['form'] = CustomUserLoginForm(request, data=request.POST)
        if aux['form'].is_valid():
            username = aux['form'].cleaned_data.get('username')
            password = aux['form'].cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect(to="home")
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    
    return render(request, 'register-login/login.html', aux)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Redirige a la página de inicio
        else:
            return render(request, 'register-login/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'register-login/register.html', {'form': form})
"""     def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirige al usuario a la página de inicio de sesión.
    else:
        form = RegistroForm()
    return render(request, 'register-login/register.html', {'form': form}) """

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect(to="home")