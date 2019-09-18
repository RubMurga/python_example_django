# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from cafeteria_puebla import views,busquedas_ajax

urlpatterns = patterns('',
    url(r'^inicio/$', views.inicio, name = 'cafeteria_puebla_inicio'),
    url(r'^agregar-producto/$', views.agregar_producto, name = 'cafeteria_puebla_agregar_producto'),
    url(r'^busqueda/', views.busqueda),
    url(r'^agregar-articulo/$', views.agregar_articulo, name = 'cafeteria_puebla_agregar_articulo'),
    url(r'^caja-registradora/$', views.caja_registradora, name = 'cafeteria_puebla_registradora'),
    url(r'^buscando/caja-registradora/$',busquedas_ajax.busquedaCaja),
    url(r'^buscar/articulo/$', busquedas_ajax.busqueda_articulo),
    url(r'^buscando/producto/$',busquedas_ajax.busqueda_producto),
    url(r'^buscando/producto/codigo-barras/$',busquedas_ajax.busqueda_producto_cb),
    url(r'Pproductos/(?P<producto_slug>[\w\-]+)/$', views.muestro_producto, name = 'cafeteria_puebla_producto'),
    url(r'^caja-registradora/venta/$', views.ventas_caja),
    url(r'^cambiar-producto/precio/$',views.cambiar_precio_producto, name = 'cafeteria_puebla_cambiar_precio_producto'),
    url(r'^borrar-producto/$', views.borrar_producto, name = 'cafeteria_puebla_borrar_producto'),

)