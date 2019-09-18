# -*- coding: utf-8 -*-
__author__ = 'RubenMurga'

from django.conf.urls import patterns, include, url
from  libreria_puebla import views
from  libreria_puebla import busquedasAjax


urlpatterns = patterns('',
    url(r'^inicio/$', views.inicio, name = 'libreria_puebla_inicio'),
    url(r'^agregar-categoria/$', views.agregar_categoria, name = 'libreria_puebla_agregar_categoria'),
    url(r'^agregar-libro/$', views.agregar_libro, name = 'libreria_puebla_agregar_libro'),
    url(r'^buscando/libro/$', busquedasAjax.busqueda_libro),
    url(r'^buscando/libro/codigo-barras/$', busquedasAjax.busqueda_libro_cb),
    url(r'^buscando/categoria/$', busquedasAjax.busqueda_categoria),
    url(r'^buscando/caja-registradora/$', busquedasAjax.busquedaCaja),
    url(r'^categoria/(?P<categoria_nombre_slug>[\w\-]+)/$', views.muestra_categoria, name='libreria_puebla_categoria'),
    url(r'^caja-registradora/$',views.caja_ventas, name = 'libreria_puebla_registradora'),
    url(r'^agregar-articulo/$',views.agregar_articulo, name = 'libreria_puebla_agregar_articulo'),
    url(r'^libros/(?P<libro_slug>[\w\-]+)/$', views.muestra_libro, name = 'libreria_puebla_libro'),
    url(r'^agregar-producto/busqueda-articulo/$', busquedasAjax.busqueda_libreria),
    url(r'^buscar/categoria-angular/$', busquedasAjax.busqueda_categoria_angular),
    url(r'^caja-registradora/venta/$', views.ventas_caja),
    url(r'^cambiar-libro/precio/$', views.cambiar_precio_libro, name = 'libreria_puebla_cambio_precio'),
    url(r'^borrar-libro/$', views.borrar_libro, name= 'libreria_puebla_borrar_libros')
)