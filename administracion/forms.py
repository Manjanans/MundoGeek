from django import forms

class subirImagen(forms.Form):
    titulo_Manga = forms.CharField()
    imagen = forms.ImageField()