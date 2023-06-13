from django.shortcuts import render

def videojuegosPC(request):
    context={}
    return render(request,"pc.html",context)

# Create your views here.
