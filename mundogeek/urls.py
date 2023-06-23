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
from administracion.views import *

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
    path('administracion/index',adminIndex,name="adminIndex"),
    path('administracion/pedidos/', listar_pedidos, name='listar_pedidos'),
    path('administracion/switch/', listar_switch, name='listado_switch'),
    path('administracion/pc/', listar_pc, name='listado_pc'),
    path('administracion/mangas/', listar_manga, name='listado_mangas'),
    path('administracion/play/', listar_play, name='listado_play'),
    path('administracion/agregar/play/', agregar_play, name='agregar_play'),
    path('administracion/agregar/manga/', agregar_manga, name='agregar_manga'),
    path('administracion/agregar/pc/', agregar_pc, name='agregar_pc'),
    path('administracion/agregar/switch/', agregar_switch, name='agregar_switch'),
    path('administracion/editar/pedidos/<int:idPedido>/', editar_pedido, name='editar_pedido'),
    path('administracion/editar/mangas/<int:idmanga>',editar_manga,name="editar_manga"),
    path('administracion/editar/pc/<int:idcomputador>/', editar_pc, name='editar_pc'),
    path('administracion/editar/playstation/<int:idplay>/', editar_play, name='editar_play'),
    path('administracion/editar/switch/<int:idswitch>/', editar_switch, name='editar_switch'),
    path('administracion/eliminar/pedidos/<int:idPedido>/', eliminar_pedido, name='eliminar_pedido'),
    path('administracion/eliminar/mangas/<int:idmanga>/', eliminar_manga, name='eliminar_manga'),
    path('administracion/eliminar/pc/<int:idcomputador>/', eliminar_pc, name='eliminar_pc'),
    path('administracion/eliminar/playstation/<int:idplay>/', eliminar_play, name='eliminar_play'),
    path('administracion/eliminar/switch/<int:idswitch>/', eliminar_switch, name='eliminar_switch'),
    
    
]
