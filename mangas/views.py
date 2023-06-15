from django.shortcuts import render

def indexMangas(request):
    context={}
    return render(request,"mangas.html",context)

# Create your views here.
