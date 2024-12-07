from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import include, path
from rest_framework import routers
from .views import *

# CONFIGURACIÓN PARA API
router = routers.DefaultRouter()
router.register('Producto', ProductosViewset)
router.register('vehiculos', VehiculoViewset) 




urlpatterns = [
    # AUTH
    path('login', login_view, name="login2"),
    path('accounts/login/', login_redirect, name="login_redirect"),
    path('register', register, name="register"),
    path('logout', logout_view, name="logout2"),

    # RECUPERAR CONTRASEÑA Y CAMBIAR
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="registration/recuperar_contrasena.html"), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
    path('account_locked', account_locked, name="account_locked"),
    
    # PAGINAS
    path('', home, name="home"),
    path('about', about, name="about"),
    path('agendar_hora', agendar_hora, name="agendar_hora"),
    path('contactos', contactos, name="contactos"),
    path('formulario', formulario, name="formulario"),


    # API
    path('api' , include(router.urls)),
    path('generalapi' , generalapi, name="generalapi"), 
    # path('api/productos', ProductoList.as_view(), name='productos_api'),
    # path('usuarios_api', usuarios_api, name="usuarios_api"),

    # VEHICULOS
    path('taller', taller, name="taller"),
    path('taller/agregar', agregar_taller, name="add_taller"),
    path('ver_perfil', ver_perfil, name="ver_perfil"),

    # PRODUCTOS
    path('mis_talleres', lista_inscripciones, name= "mis_talleres"),
    path('productos/agregar/<int:producto_id>', agregar_producto, name="pro_add"),

    # INSCRIPCIONES
    path('eliminar_inscripcion/<int:pk>/', eliminar_inscripcion, name="eliminar_inscripcion"),
    path('inscripcion_taller', inscripcion_taller, name="inscripcion_taller"),
]