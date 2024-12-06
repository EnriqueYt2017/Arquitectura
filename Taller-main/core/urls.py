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
    path('historial_compras', historial_compras, name="historial_compras"),

    # API
    path('api' , include(router.urls)),
    path('generalapi' , generalapi, name="generalapi"), 
    # path('api/productos', ProductoList.as_view(), name='productos_api'),
    # path('usuarios_api', usuarios_api, name="usuarios_api"),

    # VEHICULOS
    path('informacion_auto', informacion_auto, name="informacion_auto"),
    path('vehiculos', taller, name="vehiculos"),
    path('taller/agregar', agregar_taller, name="add_taller"),
    path('ver_perfil', ver_perfil, name="ver_perfil"),

    # PRODUCTOS
    path('productos', lista_inscripciones, name= "productos"),
    path('productos/agregar/<int:producto_id>', agregar_producto, name="pro_add"),

    # INSCRIPCIONES
    path('eliminar_inscripcion/<int:pk>/', eliminar_inscripcion, name="eliminar_inscripcion"),
    path('inscripcion/agregar', inscripcion_taller, name="add_inscripcion"),
    

    # CARRITO
    path('carrito', carrito, name="carrito"),
    path('carrito/agregar/<int:producto_id>', agregar_carrito, name="car_add"),
    path('carrito/eliminar/<int:producto_id>', eliminar_carrito, name="car_del"),
    path('carrito/restar/<int:producto_id>', restar_carrito, name="car_res"),
    path('carrito/limpiar', limpiar_carrito, name= "car_cls"),
    path('carrito_completar', carrito_completar, name="carrito_completar"),
    path('comprar', comprar, name="comprar"),
    path('compra/<int:venta_id>', compra, name="compra"),
    path('compra/<int:venta_id>/pdf', GeneratePdf.as_view(), name='compra_pdf'),
]