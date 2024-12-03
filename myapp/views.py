from django.shortcuts import render, redirect
from django.views import generic
import datetime
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
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def hello(request, username):
    return HttpResponse("Hello, Django! % s" % username) 

def home(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'pages/contacto.html')

def accesibilidad(request):
    return render(request, 'pages/accesibilidad.html')

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


# Credenciales de API
CLIENT_SECRETS_FILE = 'Talleres 10520'
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def calendario_view(request):
    creds = None
    # Si hay credenciales guardadas, úsalas
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Si no hay credenciales, obténlas del usuario
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Guarda las credenciales para la próxima vez
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Crea el servicio de Google Calendar
    service = build('calendar', 'v3', credentials=creds)

    # Obtener eventos del calendario
    events = service.events().list(calendarId='primary', singleEvents=True,
                                   orderBy='startTime').execute()
    items = events.get('items', [])

    # Procesar los eventos y mostrarlos en el calendario
    # ...

    return HttpResponse("Calendario de Google")

def obtener_eventos_dia(request):
    fecha = request.GET.get('fecha')
    # Obtener eventos del día seleccionado de la API de Google Calendar
    # ...
    eventos = [
        # ... eventos del día seleccionado
    ]
    return JsonResponse(eventos, safe=False)

def obtener_eventos_taller(request):
    fecha = request.GET.get('fecha')
    if fecha:
        talleres = Taller.objects.filter(fecha_inicio__lte=fecha, fecha_fin__gte=fecha)
        eventos = []
        for taller in talleres:
            eventos.append({
                'title': taller.nombre,
                'start': taller.fecha_inicio.strftime('%Y-%m-%d'),
                'end': taller.fecha_fin.strftime('%Y-%m-%d'),
                'color': 'blue'  # Puedes personalizar el color
            })
        return JsonResponse(eventos, safe=False)

@login_required
def registrar_taller(request):
    if request.method == 'POST':
        taller_id = request.POST.get('workshop')  # Get the workshop ID
        email = request.POST.get('email')

        if taller_id:
            try:
                taller = Taller.objects.get(pk=taller_id)  # Find the workshop by ID
            except ObjectDoesNotExist:
                messages.error(request, 'The selected workshop does not exist.')
                return redirect('registrar_taller')  # Redirect to the same form

            # Valida el email (opcional)
            # ...

            # Guarda la inscripción en la base de datos
            inscripcion = Inscripcion_taller.objects.create(
                fecha_inscripcion=timezone.now(),
                estado='pendiente',  # Puedes configurar el estado inicial
                usuario=request.user,  # Usa el usuario actual
                taller=taller,
            )
            messages.success(request, 'You have successfully registered for the workshop!')
            return redirect('talleres')  # Redirect to the workshops page
        else:
            messages.error(request, 'You must select a workshop.')
            return redirect('registrar_taller')  # Redirect to the same form
    else:
        talleres = Taller.objects.all()
        # Convierte los objetos Taller a un formato que FullCalendar pueda entender
        eventos = [
            {
                'title': taller.nombre,
                'start': taller.fecha_inicio.strftime('%Y-%m-%d'),
                'end': taller.fecha_fin.strftime('%Y-%m-%d'),
                'color': 'blue'  # Puedes cambiar el color si quieres
            }
            for taller in talleres
        ]
        return render(request, 'talleres.html', {'talleres': talleres, 'eventos': eventos})
        