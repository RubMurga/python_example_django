# -*- coding: utf-8 -*-
__author__ = 'RubenMurga'

from django.conf.urls import patterns, include, url
from  comercializadora import views
from  comercializadora import busquedasAjax


urlpatterns = patterns('',
    url(r'^inicio/$', views.inicio, name = 'comercializadora_inicio'),
    url(r'^agregar-categoria/$', views.agregar_categoria, name = 'comercializadora_agregar_categoria'),
    url(r'^agregar/$', views.agregar_producto, name = 'comercializadora_agregar'),
    url(r'^buscando/producto/$', busquedasAjax.busqueda_articulo),
    url(r'^buscando/producto/codigo-barras/$', busquedasAjax.busqueda_articulo_cb),
    url(r'^buscando/categoria/$', busquedasAjax.busqueda_categoria),
    url(r'^buscando/caja-registradora/$', busquedasAjax.busquedaCaja),
    url(r'^categoria/(?P<categoria_nombre_slug>[\w\-]+)/$', views.muestra_categoria, name='comercializadora_categoria'),
    url(r'^caja-registradora/$',views.caja_ventas, name = 'comercializadora_registradora'),
    url(r'^agregar-articulo/$',views.agregar_articulo, name = 'comercializadora_agregar_articulo'),
    url(r'^Productos/(?P<producto_slug>[\w\-]+)/$', views.muestra_producto, name = 'comercializadora_producto'),
    url(r'^agregar-producto/busqueda-articulo/$', busquedasAjax.busqueda_comercializadora),
    url(r'^buscar/categoria-angular/$', busquedasAjax.busqueda_categoria_angular),
    url(r'^caja-registradora/venta/$', views.ventas_caja),
    url(r'^cambiar-articulo/precio/$', views.cambiar_precio_producto, name = 'comercializadora_cambio_precio'),
    url(r'^borrar-articulo/$', views.borrar_producto, name= 'comercializadora_borrar_producto')
)