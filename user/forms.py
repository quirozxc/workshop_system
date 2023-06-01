from typing import Any, Optional
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import User, PhoneNumber


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        #
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        #
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
    #
#
class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'Nombre',
        },)
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'Apellido',
        },)
        self.fields['dni'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'Documento de Identidad',
        },)
        #
    #
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'dni',]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'dni': 'Documento de Identidad',
        }
    #
#
class PhoneNumberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['idc'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Identificador de País',
        },)
        self.fields['number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Identificador de País',
        },)
        self.fields['is_whatsapp_number'].widget.attrs.update({
            'class': 'form-check-input',
        },)
    #
    class Meta:
        model = PhoneNumber
        fields = ['idc', 'number', 'is_whatsapp_number',]
        labels = {
            'idc': 'Identificador de País',
            'number': 'Número Telefónico',
            'is_whatsapp_number': '¿Es un número de Whatsapp?',
        }
    #
#
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña antigua',
        },)
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña nueva',
        },)
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña nueva (confirmación)',
        },)
    #
#