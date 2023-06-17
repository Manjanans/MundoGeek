from django.db import models
from juegos.models import *
from mangas.models import *


# Create your models here.

class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    rut = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=500)
    manga = models.ForeignKey(Manga,on_delete=models.CASCADE,null=True,blank=True)
    play = models.ForeignKey(JuegoPlay,on_delete=models.CASCADE,null=True,blank=True)
    pc = models.ForeignKey(JuegoPC,on_delete=models.CASCADE,null=True,blank=True)
    switch = models.ForeignKey(JuegoSwitch,on_delete=models.CASCADE,null=True,blank=True)

