from django.contrib import admin
from django.urls import path,include
from . import views
from .views import logout_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('hello/<str:username>', views.hello),
    path('home', views.home, name='home'),
    path('pages/contacto', views.contacto, name='contacto'),
    path('pages/talleres', views.talleres, name='talleres'),
    path('pages/servicios_apoyo', views.servicios_apoyo, name='servicios_apoyo'),
    path('register-login/login', views.login, name='login'),
    path('register-login/register', views.register, name='registrar'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
