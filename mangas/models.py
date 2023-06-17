from django.db import models

class Manga(models.Model):
    idmanga = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='static/manga')
    precio = models.IntegerField()
    inventario = models.IntegerField()

# Create your models here.
