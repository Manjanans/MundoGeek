from django.shortcuts import render
from .models import *

def videojuegosPC(request):
    pc = JuegoPC.objects.all()
    context={'juegosPC':pc}
    return render(request,"pc.html",context)

def videojuegosPS4(request):
    play = JuegoPlay.objects.all()
    context={'juegoPlay':play}
    return render(request,"playstation4.html",context)

def videojuegosSwitch(request):
    swich = JuegoSwitch.objects.all()
    context={'juegosSwitch':swich}
    return render(request,"switch.html",context)
# Create your views here.
