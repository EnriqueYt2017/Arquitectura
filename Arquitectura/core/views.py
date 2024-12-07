import json
from datetime import datetime

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from core.Carrito import Carrito

from .form import *
from .models import *
from .serializers import *
from .utils import render_to_pdf


# 404 view
def custom_404(request, exception):
    return render(request, 'core/pages/404.html', status=404)

#API
#UTILIZAMOS LOS VIEWSET PARA MANEJAR LAS SOLICITUDES HTTP (GET,POST,PUT,DELETE)
class VehiculoViewset(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all().order_by('id')
    serializer_class = VehiculoSerializer
    renderer_classes = [JSONRenderer]

def generalapi(request):
    # Realizar las solicitudes GET a las APIs
    response = requests.get('https://digimon-api.vercel.app/api/digimon')
    
    # Convertir las respuestas a JSON
    digimons = response.json()

    # Paginador para Digimons
    paginator = Paginator(digimons, 4)  # Muestra 4 datos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Contexto para la plantilla
    aux = {
        'page_obj': page_obj,
    }

    # Renderizar la plantilla con el contexto
    return render(request, 'core/pages/crudapi/index.html', aux)
class ProductosViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers
    renderer_classes = [JSONRenderer]

# AUTH
def login_view(request):
    aux = {
        'form' : CustomUserLoginForm()
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
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect(to="home")
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    
    return render(request, 'registration/login.html', aux)


def login_redirect(request):
    return redirect('login2')

def register(request):
    aux = {
        'form' : CustomUserCreationForm()
    }

    if request.user.is_authenticated:
        messages.info(request, 'Por favor, cierre sesión para registrarse.')
        return redirect(to="home")

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            #ASIGNAMOS UN GRUPO AL USUARIO CREADO
            grupo = Group.objects.get(name='Adulto_Mayor')
            user.groups.add(grupo)
            # MENSAJE
            messages.success(request, 'Usuario Registrado')    
            # AUTENTICA Y LOGEA
            user = authenticate(request=request, username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request, user)
            # LO MANDA A UNA PAGINA
            return redirect(to="home")
        else:
            aux['form'] = formulario
    return render(request, 'registration/register.html', aux)

def logout_view(request):
    logout(request)
    return redirect(to="home")

def account_locked(request):
    aux = {
        'LOCKOUT_TIME': int(settings.AXES_COOLOFF_TIME.total_seconds() // 60)
    }
    return render(request, 'registration/account_locked.html', aux)

# RECUPERAR CONTRASEÑA Y CAMBIAR
def recuperar_contrasena(request):
    return render(request, 'registration/recuperar_contrasena.html')

def cambiar_clave(request):
    return render(request, 'registration/cambiar_clave.html')

# PAGINAS
def home(request):
    taller = Taller.objects.all().order_by('-id')[:3]
    aux = {
        'lista' : taller,
    }
    return render(request, 'core/pages/home.html', aux)

def about(request):
    instructores = Instructor.objects.all()
    aux = {
        'breadcrumb' : {
            'title' : 'Asesoria y Consultas',
            'links' : ['Asesoria y Consultas']
        },
        'instructores': instructores
    }
    return render(request, 'core/pages/about.html', aux)

def agendar_hora(request):
    return render(request, 'core/pages/agendar_hora.html')

@login_required
def contactos(request):
    aux = {
        'breadcrumb' : {
            'title' : 'Contáctenos',
            'links' : ['Contáctenos']
        },
        'form' : ContactForm()
    }
    if request.method == "POST":
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            message = form.cleaned_data['message']

            EmailMessage(
                'Contact Form Submission from {}'.format(name),
                message,
                'form-response@example.com', # Send from (your website)
                [settings.EMAIL_HOST_USER], # Send to (your admin email)
                [],
                reply_to=[email] # Email from the form to get back to
            ).send()
            messages.success(request, 'Se ha enviado tu correo.')
            return redirect('contactos')
        else:
            messages.error(request, 'Por favor, revisa los campos.')
            form = ContactForm(request.POST)

    return render(request, 'core/pages/contactos.html', aux)

def formulario(request):
    return render(request, 'core/pages/formulario.html')




@login_required
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    messages.success(request, 'Producto agregado al carrito')
    return redirect("productos")


# TALLER
@login_required
def taller(request):
    busqueda = request.GET.get('buscar')
    taller = Taller.objects.all().order_by('nombre')  # Ordena la consulta
    #BUSQUEDA
    if busqueda:
        taller = Taller.objects.filter(
            Q(nombre__icontains = busqueda)
        ).order_by('nombre')  # Ordena la consulta después del filtrado
    # PAGINADOR
    paginator = Paginator(taller, 3) # MUESTRA 3 DATOS
    page_number = request.GET.get('page') # OBTENEMOS LA PAGINA
    page_obj = paginator.get_page(page_number)
    aux = {
        'page_obj' : page_obj,
        'breadcrumb' : {
            'title' : 'Listado de Talleres',
            'links' : ['Listado']
        },
        'busqueda': busqueda,
        'taller': taller,
        'image': 'core/img/Adulto_MAyor/predeterminada.jpeg'
    }
    

    return render(request, 'core/pages/taller.html',aux)

def agregar_taller(request):
    if request.method == 'POST':
        form = TallerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Taller creado correctamente.')
            return redirect('taller')  # Reemplaza 'talleres_lista' con la URL de tu lista de talleres
    else:
        form = TallerForm()
    context = {'form': form}
    return render(request, 'core/pages/agregar_taller.html', context)

@login_required
def lista_inscripciones(request):
    busqueda = request.GET.get('buscar')
    inscripciones = Inscripcion_taller.objects.all()

    paginator = Paginator(inscripciones, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    aux = {
        'page_obj' : page_obj,
        'busqueda': busqueda
    }
    return render(request, 'core/pages/mis_talleres.html', aux)

@login_required
def eliminar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion_taller, pk=pk)
    inscripcion.delete()
    messages.success(request, 'Inscripción eliminada correctamente.')
    return redirect('mis_talleres')
    

@login_required  # Asegúrate de que el usuario esté autenticado
def inscripcion_taller(request):
    taller = Taller.objects.all()
    inscripcion_taller = Inscripcion_taller.objects.filter(usuario=request.user)
    
    if request.method == 'POST':
        form = InscripcionTallerForm(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.usuario = request.user
            inscripcion.save()
            messages.success(request, 'Inscripción realizada correctamente.')
            return redirect('taller')
    else:
        form = InscripcionTallerForm(initial={'usuario': request.user})
        form.fields['usuario'].widget = forms.HiddenInput()
        
    aux = {'form': form,
           'taller': taller,
           'inscripcion_taller': inscripcion_taller}
    return render(request, 'core/pages/inscripcion_taller.html', aux)



@login_required
def ver_perfil(request):
        user = request.user
        inscripciones = Inscripcion_taller.objects.filter(usuario=user)
        inscripcionesTaller = Inscripcion_taller.objects.all()

        if request.method == 'POST':
            form = EditarPerfilForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Perfil actualizado correctamente.')
                return redirect('ver_perfil')
            else:
                messages.error(request, 'Por favor, revisa los campos.')
        else:
            form = EditarPerfilForm(instance=user)

        context = {
            'user': user,
            'inscripciones': inscripciones,
            'inscripcionesTaller': inscripcionesTaller,
            'form': form
        }
        return render(request, 'core/pages/ver_perfil.html', context)



