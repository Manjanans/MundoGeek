from django.db import models

class Cliente(models.Model):
    usuario = models.CharField(primary_key=True,max_length=500)
    nombres = models.CharField(max_length=100)
    apPaterno = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)
# Create your models here.
