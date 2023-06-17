"""mundogeek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from juegos.views import *
from mangas.views import *
from common.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('videojuegos/pc', videojuegosPC, name="indexPC"),
    path('mangas/listado',indexMangas,name="indexMangas"),
    path('videojuegos/PS4',videojuegosPS4,name="indexPS4"),
    path('videojuegos/Switch',videojuegosSwitch,name="indexSwitch"),
    path('pedidos/pedidoManga/<int:ident>',pedidoManga, name="pedidoManga"),
    path('pedidos/pedidoPc/<int:ident>',pedidoPc, name="pedidoPc"),
    path('pedidos/pedidoPlay/<int:ident>',pedidoPlay, name="pedidoPlay"),
    path('pedidos/pedidoSwitch/<int:ident>',pedidoSwitch, name="pedidoSwitch"),
    path('pedidos/pedidoManga/confirmado',confirmacionExitosa, name="confirmado"),
    path('pedidos/pedidoPc/confirmado',confirmacionKeyPc, name="confirmado"),
    path('pedidos/pedidoPlay/confirmado',confirmacionExitosa, name="confirmado"),
    path('pedidos/pedidoSwitch/confirmado',confirmacionExitosa, name="confirmado"),
]
