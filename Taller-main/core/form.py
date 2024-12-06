from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import (CharField, EmailField, Form, ModelForm, PasswordInput, Textarea)
from django_recaptcha.fields import ReCaptchaField

from .models import *


class VehiculoForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Vehiculo
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ['username','email']

class CustomUserLoginForm(AuthenticationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = '__all__'

class MantenimientoForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Mantenimiento
        fields = '__all__'

class ContactForm(Form):
    captcha = ReCaptchaField()
    name = CharField(required=True)
    email = EmailField(required=True)
    asunto = CharField(required=True)
    message = CharField(widget=Textarea)

class TallerForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Taller
        fields = '__all__'
class inscripcionForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Inscripcion_taller
        fields = '__all__'