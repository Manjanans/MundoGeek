from django.shortcuts import get_object_or_404, redirect, render
from common.models import *
from juegos.models import *
from mangas.models import *
from .forms import *

def adminIndex(request):
    return render(request,'administracion.html')

def agregar_manga(request):
    if request.method == "POST":
        formulario = subirImagen(request.POST,request.FILES)
        if formulario.is_valid():
            img = formulario.cleaned_data.get("imagen")
            contador = 0
            mangas = Manga.objects.all()
            try:
                for m in mangas:
                    contador = m.idmanga
                contador+=3
            except:
                contador = 1
            titulo = formulario.cleaned_data.get("titulo_Manga")
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            obj = Manga(contador, titulo,descripcion,img,precio,inventario,"Manga")
            obj.save()
            return redirect('adminIndex')
        else:
            return redirect('index')
        
        
        
    context = {}
    context['form'] = subirImagen()
    return render(request,'agregar_manga.html',context)

def agregar_switch(request):
    return render(request,'agregar_switch.html')

def agregar_play(request):
    return render(request,'agregar_play.html')

def agregar_pc(request):
    return render(request,'agregar_pc.html')

def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'listar_pedidos.html', {'pedidos': pedidos})

def listar_switch(request):
    switch = JuegoSwitch.objects.all()
    return render(request, 'listar_pedidos.html', {'juegos': switch})

def listar_play(request):
    play = JuegoPlay.objects.all()
    return render(request, 'listar_pedidos.html', {'juegos': play})

def listar_pc(request):
    pc = JuegoPC.objects.all()
    return render(request, 'listar_pedidos.html', {'juegos': pc})

def listar_manga(request):
    manga = Manga.objects.all()
    return render(request, 'listar_pedidos.html', {'manga': manga})

def editar_pedido(request, idPedido):
    pedido = get_object_or_404(Pedido, idPedido=idPedido)

    if request.method == 'POST':
        
        nombres = request.POST["name"]
        apellidos = request.POST["surname"]
        rut = request.POST["rut"]
        telefono = request.POST["telefono"]
        regg = request.POST["regiones"]
        comuna = request.POST["comuna"]
        direccion = request.POST["direccion"]

        
        pedido.nombres = nombres
        pedido.apellidos = apellidos
        pedido.rut = rut
        pedido.telefono = telefono
        pedido.region = regg
        pedido.comuna = comuna
        pedido.direccion = direccion
        pedido.save()

        return redirect('listar_pedidos')

    return render(request, 'editar_pedido.html', {'pedido': pedido})

def eliminar_pedido(request, idPedido):
    pedido = get_object_or_404(Pedido, idPedido=idPedido)

    if request.method == 'POST':
        # Eliminar el pedido
        pedido.delete()

        return redirect('listar_pedidos')

    return render(request, 'eliminar_pedido.html', {'pedido': pedido})

# Create your views here.
