from django.shortcuts import render

def videojuegosPC(request):
    context={}
    return render(request,"pc.html",context)

def videojuegosPS4(request):
    context={}
    return render(request,"playstation4.html",context)

def videojuegosSwitch(request):
    context={}
    return render(request,"switch.html",context)
# Create your views here.
