from django import forms
from django.contrib.auth.forms import AuthenticationForm
from user.models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        #
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        #
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
