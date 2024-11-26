from django.forms import ModelForm, DateInput, FileInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib.auth.models import User
from django import forms

""" class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario','nombre', 'apellido', 'password', 'email', 'fecha_registro', 'foto_perfil']
        widgets = {
            'fecha_registro': forms.DateInput(attrs={'type': 'date'}),
            'foto_perfil': forms.FileInput(attrs={'accept': 'image/*'}),
        } """


# spell-checker: disable
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'
        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data

        def save(self, commit=True):
            user = super().save(commit=False)
            if commit:
                user.save()
            return user
