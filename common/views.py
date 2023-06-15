from django.shortcuts import render
from .models import *

def index(request):
    context={}
    return render(request,"index.html",context)

def createUser(request):
    context={}
    return render(request,'creausuario.html',context)

def iniciaSesion(request):
    context={}
    return render(request,"login.html",context)

def creacionexitosa(request):
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
        return render(request,'usuarioExitoso.html',context)



# Create your views here.
