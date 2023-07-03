from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form

class subirImagen(forms.Form):
    titulo = forms.CharField()
    imagen = forms.ImageField()
  
class creacionDeUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        labels = {
            'username': 'Ingrese el nombre de Usuario:',
            'first_name': 'Ingrese el nombre de la persona:',
            'last_name': 'Ingrese el apellido de la persona:',
            'email': 'Ingrese el email de la persona:',
            }
    