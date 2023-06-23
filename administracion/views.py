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
            titulo = formulario.cleaned_data.get("titulo")
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
    if request.method == "POST":
        formulario = subirImagen(request.POST,request.FILES)
        if formulario.is_valid():
            img = formulario.cleaned_data.get("imagen")
            contador = 0
            mangas = Manga.objects.all()
            try:
                for m in mangas:
                    contador = m.idmanga
                contador+=4
            except:
                contador = 1
            titulo = formulario.cleaned_data.get("titulo")
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            obj = JuegoSwitch(contador, titulo,descripcion,img,precio,inventario,"JuegoSwitch")
            obj.save()
            return redirect('adminIndex')
        else:
            return redirect('index')  
    context = {}
    context['form'] = subirImagen()
    return render(request,'agregar_switch.html',context)

def agregar_play(request):
    if request.method == "POST":
        formulario = subirImagen(request.POST,request.FILES)
        if formulario.is_valid():
            img = formulario.cleaned_data.get("imagen")
            contador = 0
            mangas = Manga.objects.all()
            try:
                for m in mangas:
                    contador = m.idmanga
                contador+=5
            except:
                contador = 1
            titulo = formulario.cleaned_data.get("titulo")
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            obj = JuegoSwitch(contador, titulo,descripcion,img,precio,inventario,"JuegoPlay")
            obj.save()
            return redirect('adminIndex')
        else:
            return redirect('index')  
    context = {}
    context['form'] = subirImagen()
    return render(request,'agregar_play.html',context)

def agregar_pc(request):
    if request.method == "POST":
        formulario = subirImagen(request.POST,request.FILES)
        if formulario.is_valid():
            img = formulario.cleaned_data.get("imagen")
            contador = 0
            mangas = Manga.objects.all()
            try:
                for m in mangas:
                    contador = m.idmanga
                contador+=6
            except:
                contador = 1
            titulo = formulario.cleaned_data.get("titulo")
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            obj = JuegoSwitch(contador, titulo,descripcion,img,precio,inventario,"JuegoPC")
            obj.save()
            return redirect('adminIndex')
        else:
            return redirect('index')  
    context = {}
    context['form'] = subirImagen()
    return render(request,'agregar_pc.html',context)

def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'listar_pedidos.html', {'pedidos': pedidos})

def listar_switch(request):
    switch = JuegoSwitch.objects.all()
    return render(request, 'listar_switch.html', {'juegos': switch})

def listar_play(request):
    play = JuegoPlay.objects.all()
    return render(request, 'listar_play.html', {'juegos': play})

def listar_pc(request):
    pc = JuegoPC.objects.all()
    return render(request, 'listar_pc.html', {'juegos': pc})

def listar_manga(request):
    manga = Manga.objects.all()
    return render(request, 'listar_manga.html', {'mangas': manga})

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

def editar_manga(request,idmanga):
    manga = get_object_or_404(Manga,idmanga = idmanga)
    context = {'manga':manga}
    context['form'] = subirImagen(initial={'titulo': manga.titulo, 'imagen':manga.imagen})

    if request.method == "POST":
        formulario = subirImagen(request.POST,request.FILES)
        if formulario.is_valid():
            img = formulario.cleaned_data.get("imagen")
            titulo = formulario.cleaned_data.get("titulo")
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            manga.titulo = titulo
            manga.descripcion = descripcion
            manga.precio = precio
            manga.inventario = inventario
            manga.imagen = img
            manga.save()
            return redirect('listado_mangas')
        else:
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            manga.descripcion = descripcion
            manga.precio = precio
            manga.inventario = inventario
            manga.save()
            return redirect('listado_mangas')

    return render(request,'editar_manga.html',context)

def editar_pc(request,idcomputador):
    pc = get_object_or_404(JuegoPC,idcomputador = idcomputador)
    context = {'pc':pc}
    context['form'] = subirImagen(initial={'titulo': pc.titulo, 'imagen':pc.imagen})

    if request.method == "POST":
        formulario = subirImagen(request.POST,request.FILES)
        if formulario.is_valid():
            img = formulario.cleaned_data.get("imagen")
            titulo = formulario.cleaned_data.get("titulo")
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            pc.titulo = titulo
            pc.descripcion = descripcion
            pc.precio = precio
            pc.inventario = inventario
            pc.imagen = img
            pc.save()
            return redirect('listado_pc')
        else:
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            pc.descripcion = descripcion
            pc.precio = precio
            pc.inventario = inventario
            pc.save()
            return redirect('listado_pc')

    return render(request,'editar_pc.html',context)

def editar_play(request,idplay):
    play = get_object_or_404(JuegoPlay,idplay = idplay)
    context = {'play':play}
    context['form'] = subirImagen(initial={'titulo': play.titulo, 'imagen':play.imagen})

    if request.method == "POST":
        formulario = subirImagen(request.POST,request.FILES)
        if formulario.is_valid():
            img = formulario.cleaned_data.get("imagen")
            titulo = formulario.cleaned_data.get("titulo")
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            play.titulo = titulo
            play.descripcion = descripcion
            play.precio = precio
            play.inventario = inventario
            play.imagen = img
            play.save()
            return redirect('listado_play')
        else:
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            play.descripcion = descripcion
            play.precio = precio
            play.inventario = inventario
            play.save()
            return redirect('listado_play')

    return render(request,'editar_play.html',context)

def editar_switch(request,idswitch):
    switch = get_object_or_404(JuegoSwitch,idswitch = idswitch)
    context = {'switch':switch}
    context['form'] = subirImagen(initial={'titulo': switch.titulo, 'imagen':switch.imagen})

    if request.method == "POST":
        formulario = subirImagen(request.POST,request.FILES)
        if formulario.is_valid():
            img = formulario.cleaned_data.get("imagen")
            titulo = formulario.cleaned_data.get("titulo")
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            switch.titulo = titulo
            switch.descripcion = descripcion
            switch.precio = precio
            switch.inventario = inventario
            switch.imagen = img
            switch.save()
            return redirect('listado_switch')
        else:
            descripcion = request.POST["descripcion"]
            precio = request.POST["precio"]
            inventario = request.POST["inventario"]
            switch.descripcion = descripcion
            switch.precio = precio
            switch.inventario = inventario
            switch.save()
            return redirect('listado_switch')

    return render(request,'editar_switch.html',context)


def eliminar_pedido(request, idPedido):
    pedido = get_object_or_404(Pedido, idPedido=idPedido)
    
    if request.method == 'POST':
        # Eliminar el pedido
        pedido.delete()

        return redirect('listar_pedidos')
    
    return render(request, 'eliminar_pedido.html', {'pedido': pedido})

def eliminar_manga(request, idmanga):
    manga = get_object_or_404(Manga, idmanga=idmanga)
    
    if request.method == 'POST':
        # Eliminar el pedido
        manga.delete()

        return redirect('listado_manga')
    
    return render(request, 'eliminar_manga.html', {'manga': manga})

def eliminar_pc(request, idcomputador):
    pc = get_object_or_404(JuegoPC, idcomputador=idcomputador)
    
    if request.method == 'POST':
        # Eliminar el pedido
        pc.delete()

        return redirect('listado_pc')
    
    return render(request, 'eliminar_pc.html', {'pc': pc})

def eliminar_play(request, idplay):
    play = get_object_or_404(JuegoPlay, idplay=idplay)
    
    if request.method == 'POST':
        # Eliminar el pedido
        play.delete()

        return redirect('listado_play')
    
    return render(request, 'eliminar_play.html', {'play': play})

def eliminar_switch(request, idswitch):
    switch = get_object_or_404(JuegoSwitch, idswitch=idswitch)
    
    if request.method == 'POST':
        # Eliminar el pedido
        switch.delete()

        return redirect('listado_switch')
    
    return render(request, 'eliminar_switch.html', {'switch': switch})

# Create your views here.
