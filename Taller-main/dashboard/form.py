from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group, User
from django.forms import ModelChoiceField, ModelForm
from django_recaptcha.fields import ReCaptchaField

from core.models import *

from .models import *


class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()
    group = ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'group', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser']

class CustomUserChangeForm(UserChangeForm):
    captcha = ReCaptchaField()
    group = ModelChoiceField(queryset=Group.objects.all(), required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'group', 'is_staff', 'is_active', 'is_superuser']

class ProductosForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Producto
        fields = '__all__'

class VehiculosForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Vehiculo
        fields = '__all__'

class VentasForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Venta
        fields = '__all__'