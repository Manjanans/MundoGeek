from django import forms

class subirImagen(forms.Form):
    titulo = forms.CharField()
    imagen = forms.ImageField()