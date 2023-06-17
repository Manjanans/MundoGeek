from django.db import models

class JuegoPC(models.Model):
    idcomputador = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='static/pc')
    precio = models.IntegerField()
    inventario = models.IntegerField()
    tipo = models.CharField(max_length=100)

class JuegoSwitch(models.Model):
    idswitch = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='static/switch')
    precio = models.IntegerField()
    inventario = models.IntegerField()
    tipo = models.CharField(max_length=100)

class JuegoPlay(models.Model):
    idplay = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='static/ps4')
    precio = models.IntegerField()
    inventario = models.IntegerField()
    tipo = models.CharField(max_length=100)

# Create your models here.
