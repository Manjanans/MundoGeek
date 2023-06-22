from django.contrib import admin
from .models import *

admin.site.register(Pedido)
admin.site.register(KeysPC)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'juego', 'fecha_pedido')

# Register your models here.
