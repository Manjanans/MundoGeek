from django.shortcuts import render
from .models import *

def indexMangas(request):
    man = Manga.objects.all()
    context={'mangas':man}
    return render(request,"manga.html",context)

# Create your views here.
