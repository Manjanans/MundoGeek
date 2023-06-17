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
    obj = JuegoPC.objects.get(idcomputador=ident)
    context={'item':obj}
    return render(request,'keypc.html',context)

def pedidoSwitch(request,ident):
    obj = JuegoSwitch.objects.get(idswitch = ident)
    context={'item':obj}
    return render(request,'pedido.html',context)

def confirmacionExitosa(request):
    
    nombres = request.POST["name"]
    apellidos = request.POST["surname"]
    rut = request.POST["rut"]
    telefono = request.POST["telefono"]
    emailUser = request.POST["n-email"]
    servEmail = request.POST["serv-name"]
    regg = request.POST["regiones"]
    comuna = request.POST["comuna"]
    direccion = request.POST["direccion"]
    email = emailUser+"@"+servEmail

    rutCompleto = digitoVerificador(rut)

    tipo = request.POST["prodType"]
    ident = request.POST["ident"]
    try:
        cont = Pedido.objects.all()
        for i in cont:
            caunter = i.idPedido
        caunter+=1
    except:
        caunter = 1

    if tipo=="Manga":
        item = Manga.objects.get(idmanga = ident)
        item.inventario-=1
        item.save()
        obj = Pedido(caunter,nombres,apellidos,email,regg,comuna,rutCompleto,telefono,direccion,ident,None,None)
        obj.save()
        context={'mensaje':'OK, datos guardados con éxito'}
        return render(request,'confirmado.html',context)
    elif tipo=="JuegoPlay":
        item = JuegoPlay.objects.get(idplay = ident)
        item.inventario-=1
        item.save()
        obj = Pedido(caunter,nombres,apellidos,email,regg,comuna,rutCompleto,telefono,direccion,None,ident,None)
        obj.save()
        context={'mensaje':'OK, datos guardados con éxito'}
        return render(request,'confirmado.html',context)
    elif tipo=="JuegoSwitch":
        item = JuegoSwitch.objects.get(idswitch = ident)
        item.inventario-=1
        item.save()
        obj = Pedido(caunter,nombres,apellidos,email,regg,comuna,rutCompleto,telefono,direccion,None,None,ident)
        obj.save()
        context={'mensaje':'OK, datos guardados con éxito'}
        return render(request,'confirmado.html',context)
    


def confirmacionKeyPc(request):
    nombres = request.POST["name"]
    apellidos = request.POST["surname"]
    rut = request.POST["rut"]
    telefono = request.POST["telefono"]
    emailUser = request.POST["n-email"]
    servEmail = request.POST["serv-name"]
    email = emailUser+"@"+servEmail

    rutCompleto = digitoVerificador(rut)

    identi = request.POST["identif"]

    try:
        cont = KeysPC.objects.all()
        for i in cont:
            caunter = i.idPedido
        caunter+=1
    except:
        caunter = 1

    item = JuegoPC.objects.get(idcomputador = identi)

    item.inventario-=1
    item.save()
    obj = KeysPC(caunter,nombres,apellidos,email,rutCompleto,telefono,identi)
    obj.save()
    context={'mensaje':'OK, datos guardados con éxito'}
    return render(request,'confirmado.html',context)

# Create your views here.
