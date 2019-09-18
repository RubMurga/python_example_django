# -*- coding: utf-8 -*-
__author__ = 'RubenMurga'

from django.conf.urls import patterns, include, url
from control import views, busquedas_angular
urlpatterns = patterns('',
    url(r'^inicio/$', views.inicio, name = 'control_inicio'),
    url(r'^movimientos/$', views.bitacora, name = 'bitacora_eliminados'),
    url(r'^bitacora/get_data/$', busquedas_angular.bitacora_data),

    url(r'^obtener/vendedores/$', busquedas_angular.busqueda_vendedores_dia),
    url(r'^obtener/productos-agotados/$',busquedas_angular.acabando_productos),

    url(r'^libreria/ventas-por-dia/$', views.ventas_dia_libreria, name = 'libreria_ventas_dia'),
    url(r'^libreria/ventas-por-dia/inicial/$', busquedas_angular.busqueda_inicial_libros_dia),
    url(r'^libreria/ventas-por-dia/vendedor/$', busquedas_angular.busqueda_vendedor_dia),
    url(r'^libreria/ventas-por-dia/libro/$', busquedas_angular.busqueda_libro_dia),

    url(r'^libreria/ventas-por-semana/$', views.ventas_semana_libreria, name = 'libreria_ventas_semana'),
    url(r'^libreria/ventas-por-semana/inicial/$', busquedas_angular.busqueda_libro_semana_inicial),
    url(r'^libreria/ventas-por-semana/vendedor/$', busquedas_angular.busqueda_libro_semana_vendedor),
    url(r'^libreria/ventas-por-semana/libro/$', busquedas_angular.busqueda_libro_semana_libro),

    url(r'^libreria/ventas-por-mes/$', views.ventas_mes_libreria, name = 'libreria_ventas_mes'),
    url(r'^libreria/ventas-por-mes/inicial/$', busquedas_angular.busqueda_inicial_libros_mes),
    url(r'^libreria/ventas-por-mes/vendedor/$', busquedas_angular.busqueda_vendedor_mes),
    url(r'^libreria/ventas-por-mes/libro/$', busquedas_angular.busqueda_libro_mes),

    url(r'^libreria/libros-registrados/$',views.libros_registrados, name= 'libreria_libros_registrados'),
    url(r'^libreria/libros/$', busquedas_angular.busqueda_todos_libros),
    url(r'^libreria/libros/libro/$', busquedas_angular.busqueda_todos_libro_especifico),


    url(r'^comercializadora/ventas-por-dia/$', views.ventas_dia_comercializadora, name = 'comercializadora_ventas_dia'),
    url(r'^comercializadora/ventas-por-dia/inicial/$', busquedas_angular.busqueda_inicial_comercializadora_dia),
    url(r'^comercializadora/ventas-por-dia/vendedor/$', busquedas_angular.busqueda_vendedor_comercializadora_dia),
    url(r'^comercializadora/ventas-por-dia/libro/$', busquedas_angular.busqueda_comercializadora_producto_dia),



    url(r'^comercializadora/ventas-por-semana/$', views.ventas_semana_comercializadora, name = 'comercializadora_ventas_semana'),
    url(r'^comercializadora/ventas-por-semana/inicial/$', busquedas_angular.busqueda_comercializadora_semana_inicial),
    url(r'^comercializadora/ventas-por-semana/vendedor/$', busquedas_angular.busqueda_comercializadora_semana_vendedor),
    url(r'^comercializadora/ventas-por-semana/libro/$', busquedas_angular.busqueda_comercializadora_semana_producto),


    url(r'^comercializadora/ventas-por-mes/$', views.ventas_mes_comercializadora, name = 'comercializadora_ventas_mes'),
    url(r'^comercializadora/ventas-por-mes/inicial/$', busquedas_angular.busqueda_inicial_comercializadora_mes),
    url(r'^comercializadora/ventas-por-mes/vendedor/$', busquedas_angular.busqueda_comercializadora_vendedor_mes),
    url(r'^comercializadora/ventas-por-mes/libro/$', busquedas_angular.busqueda_comercializadora_producto_mes),

    url(r'^comercializadora/ventas-por-mes-especifico/$', views.ventas_mes_spec_comercializora, name = 'comercializadora_ventas_mes_spec'),
    url(r'^comercializadora/busqueda-anio-mes/$', busquedas_angular.busqueda_comercializadora_anio_mes),

    url(r'^comercializadora/articulos-registrados/$',views.articulos_registrados, name= 'comercializadora_libros_registrados'),
    url(r'^comercializadora/articulos/$', busquedas_angular.busqueda_comercializadora_productos),
    url(r'^comercializadora/articulos/articulo/$', busquedas_angular.busqueda_todos_comercializadora_especifico),

    url(r'^cafeteria/ventas-por-dia/$', views.ventas_dia_cafeteria, name = 'cafeteria_ventas_dia'),
    url(r'^cafeteria/ventas-por-dia/inicial/$', busquedas_angular.busqueda_inicial_cafeteria_dia),
    url(r'^cafeteria/ventas-por-dia/vendedor/$', busquedas_angular.busqueda_vendedor_dia_cafeteria),
    url(r'^cafeteria/ventas-por-dia/producto/$', busquedas_angular.busqueda_producto_dia_cafeteria),

    url(r'^cafeteria/ventas-por-semana/$', views.ventas_semana_cafeteria, name = 'cafeteria_ventas_semana'),
    url(r'^cafeteria/ventas-por-semana/inicial/$', busquedas_angular.busqueda_producto_semana_inicial),
    url(r'^cafeteria/ventas-por-semana/vendedor/$', busquedas_angular.busqueda_producto_semana_vendedor),
    url(r'^cafeteria/ventas-por-semana/producto/$' , busquedas_angular.busqueda_producto_semana),

    url(r'^cafeteria/ventas-por-mes/$', views.ventas_mes_cafeteria, name = 'cafeteria_ventas_mes'),
    url(r'^cafeteria/ventas-por-mes/inicial/$', busquedas_angular.busqueda_inicial_cafeteria_mes),
    url(r'^cafeteria/ventas-por-mes/producto/$', busquedas_angular.busqueda_producto_mes_cafeteria),

    url(r'^cafeteria/productos-registrados/$', views.productos_registrados, name = 'cafeteria_productos_registrados'),
    url(r'^cafeteria/productos/$',busquedas_angular.busqueda_todos_productos),
    url(r'^cafeteria/productos/producto/$', busquedas_angular.busqueda_productos_especifico),

    # ACTUALIZAR INVENTARIOS
    url(r'^libreria/actualizar_inventario/$',views.actualizar_inventario, name='libreria_actualizar_inventario'),
    url(r'^libreria/buscar/$',busquedas_angular.busqueda_libros_actualiza),
    url(r'^libreria/buscar_id/$',busquedas_angular.busqueda_restantes_total_num),
    url(r'^libreria/actualizar_existencias/$', busquedas_angular.actualizar_existencias_libros),


    url(r'^cafeteria/actualizar_inventario/$',views.actualizar_inventario_cafeteria,name = 'cafeteria_actualizar_inventario'),
    url(r'^cafeteria/buscar/$',busquedas_angular.busqueda_cafeteria_actualiza),
    url(r'^cafeteria/buscar_id/$',busquedas_angular.cafeteria_busqueda_restantes_total_num),
    url(r'^cafeteria/actualizar_existencias/$', busquedas_angular.actualizar_existencias_cafeteria),

    url(r'^comercializadora/actualizar_inventario/$',views.actualizar_inventario_comercializadora,name = 'comercializadora_actualizar_inventario'),
    url(r'^comercializadora/buscar/$',busquedas_angular.busqueda_comercializadora_actualiza),
    url(r'^comercializadora/buscar_id/$',busquedas_angular.comercializadora_busqueda_restantes_total_num),
    url(r'^comercializadora/actualizar_existencias/$', busquedas_angular.actualizar_existencias_comercializadora),
    
)