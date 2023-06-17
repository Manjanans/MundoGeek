from django.shortcuts import render
from .models import *
from juegos.models import *
from mangas.models import *

def index(request):
    context={}
    return render(request,"index.html",context)

def digitoVerificador(rut):
    verificador=[];
    contador=2;
    suma=0;
    for i in str(rut):
        verificador.insert(0,int(i));
    for i in range(len(verificador)):
        if contador==8:
            contador=2;
        if contador<=7:
            suma+=verificador[i]*contador;
            contador+=1;
    resto=suma//11;
    resto*=11;
    verificar=suma-resto;
    completo=11-verificar;

    if completo==11:
        return str(rut)+'-0'
    elif completo==10:
       return str(rut)+'-K'
    else:
        completo=str(completo)
        return str(rut)+'-'+completo
    
def pedidoManga(request,ident): 
    obj = Manga.objects.get(idmanga = ident)
    context={'item':obj}
    return render(request,'pedido.html',context)

def pedidoPlay(request,ident):
    obj = JuegoPlay.objects.get(idplay=ident)
    context={'item':obj}
    return render(request,'pedido.html',context)

def pedidoPc(request,ident):
    obj = JuegoPC.objects.get(idpc=ident)
    context={'item':obj}
    return render(request,'pedido.html',context)

def pedidoSwitch(request,ident):
    obj = JuegoSwitch.objects.get(idswitch = ident)
    context={'item':obj}
    return render(request,'pedido.html',context)

"""def creacionexitosa(request):
    clientes = Cliente.objects.all()

    bandera = False

    user = request.POST["user"]
    name = request.POST["name"]
    surname = request.POST["surname"]
    emailUser = request.POST["n-email"]
    servEmail = request.POST["serv-name"]
    regg = request.POST["regiones"]
    comuna = request.POST["comuna"]
    pwrd = request.POST["pwrd"]
    email = emailUser+"@"+servEmail
    
    for cliente in clientes:
        if cliente.usuario == user:
            bandera = True
    if bandera:
        context={'mensaje':'El usuario ya existe. Elija uno nuevo'}
        return render(request,'creausuario.html',context)
    else:
        obj = Cliente(user,name,surname,email,regg,comuna,pwrd)
        obj.save()
        context={'mensaje':'OK, datos guardados con éxito'}
        return render(request,'usuarioExitoso.html',context)"""


# Create your views here.
