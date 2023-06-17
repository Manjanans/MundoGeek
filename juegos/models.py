from django.db import models

class JuegoPC(models.Model):
    idpc = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='static/pc')
    precio = models.IntegerField()
    inventario = models.IntegerField()

class JuegoSwitch(models.Model):
    idswitch = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='static/switch')
    precio = models.IntegerField()
    inventario = models.IntegerField()

class JuegoPlay(models.Model):
    idplay = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='static/ps4')
    precio = models.IntegerField()
    inventario = models.IntegerField()

# Create your models here.
