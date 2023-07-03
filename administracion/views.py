from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from common.models import *
from juegos.models import *
from mangas.models import *

from .forms import *

def logoutAdministracion(request):
    logout(request)
    return redirect('login')

def loginAdministracion(request):   
    if request.user.is_authenticated:
            usuario = request.user.username
            obj = User.objects.get(username=usuario)
            context={'usuario':obj}
            return redirect('adminIndex')

    if request.method == "POST":
        usuario = request.POST['user']
        contrasenia = request.POST['password']

        autenticacion = authenticate(request,username=usuario,password=contrasenia)

        if autenticacion is not None:
            obj = User.objects.get(username=usuario)
            context={'usuario':obj}
            login(request, autenticacion)
            return redirect('adminIndex')
        else:
            context = {'fallido':'EL usuario o la contraseña indicada no son correctas. Intente nuevamente.'}
            return render(request, 'login.html',context)
        
    return render(request, 'login.html')

@login_required
def adminIndex(request):
    obj = request.user.username
    context = {'user':str(obj)}
    return render(request,'administracion.html',context)

@login_required
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

@login_required
def agregar_usuarios(request):
    context = {'form':creacionDeUsuario()}
    if request.method == 'POST':
        formulario = creacionDeUsuario(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('adminIndex')
    return render(request, 'agregar_usuarios.html', context)

@login_required
def editar_usuarios(request,usuario):
    usser = User.objects.get(username = usuario)
    context = {'usser':usser}
    if request.method == 'POST':
        neim = request.POST["nombre"]
        surneim = request.POST["apellido"]
        email = request.POST["email"]
        pwrd = request.POST["contrasenia"]
        usser.first_name = neim
        usser.last_name = surneim
        usser.email = email
        usser.set_password(pwrd)
        usser.save()
        return redirect('adminIndex')
    return render(request, 'editar_usuarios.html', context)   

@login_required
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

@login_required
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

@login_required
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

@login_required
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'listar_pedidos.html', {'pedidos': pedidos})

@login_required
def listar_switch(request):
    switch = JuegoSwitch.objects.all()
    return render(request, 'listar_switch.html', {'juegos': switch})

@login_required
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'listar_usuarios.html', {'users': usuarios})

@login_required
def listar_play(request):
    play = JuegoPlay.objects.all()
    return render(request, 'listar_play.html', {'juegos': play})

@login_required
def listar_pc(request):
    pc = JuegoPC.objects.all()
    return render(request, 'listar_pc.html', {'juegos': pc})

@login_required
def listar_manga(request):
    manga = Manga.objects.all()
    return render(request, 'listar_manga.html', {'mangas': manga})

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
def eliminar_pedido(request, idPedido):
    pedido = get_object_or_404(Pedido, idPedido=idPedido)
    
    if request.method == 'POST':
        # Eliminar el pedido
        pedido.delete()

        return redirect('listar_pedidos')
    
    return render(request, 'eliminar_pedido.html', {'pedido': pedido})

@login_required
def eliminar_manga(request, idmanga):
    manga = get_object_or_404(Manga, idmanga=idmanga)
    
    if request.method == 'POST':
        # Eliminar el pedido
        manga.delete()

        return redirect('listado_manga')
    
    return render(request, 'eliminar_manga.html', {'manga': manga})

@login_required
def eliminar_pc(request, idcomputador):
    pc = get_object_or_404(JuegoPC, idcomputador=idcomputador)
    
    if request.method == 'POST':
        # Eliminar el pedido
        pc.delete()

        return redirect('listado_pc')
    
    return render(request, 'eliminar_pc.html', {'pc': pc})

@login_required
def eliminar_play(request, idplay):
    play = get_object_or_404(JuegoPlay, idplay=idplay)
    
    if request.method == 'POST':
        # Eliminar el pedido
        play.delete()

        return redirect('listado_play')
    
    return render(request, 'eliminar_play.html', {'play': play})

@login_required
def eliminar_switch(request, idswitch):
    switch = get_object_or_404(JuegoSwitch, idswitch=idswitch)
    
    if request.method == 'POST':
        # Eliminar el pedido
        switch.delete()

        return redirect('listado_switch')
    
    return render(request, 'eliminar_switch.html', {'switch': switch})

@login_required
def eliminar_usuarios(request, usuario):
    usser = get_object_or_404(User, username=usuario)
    
    if request.method == 'POST':
        # Eliminar el pedido
        usser.delete()

        return redirect('listar_usuarios')
    
    return render(request, 'eliminar_usuarios.html', {'usser': usser})

# Create your views here.
