__author__ = 'RubenMurga'

from datetime import date
from cafeteria.models import productos, Articulo as Articulo_cafeteria
from libreria.models import Producto, Articulo as Articulo_libreria
from comercializadora.models import Producto_comercializadora, Articulo_comercializadora
from django.contrib.auth.models import User
from registro.models import UserProfile

def ventas_semana():
    ventas_lunes_libreria= 0
    ventas_martes_libreria = 0
    ventas_miercoles_libreria = 0
    ventas_jueves_libreria = 0
    ventas_viernes_libreria = 0
    ventas_sabado_libreria = 0
    ventas_domingo_libreria = 0

    ventas_lunes_comercializadora= 0
    ventas_martes_comercializadora = 0
    ventas_miercoles_comercializadora = 0
    ventas_jueves_comercializadora = 0
    ventas_viernes_comercializadora = 0
    ventas_sabado_comercializadora = 0
    ventas_domingo_comercializadora = 0

    ventas_lunes_cafeteria = 0
    ventas_martes_cafeteria = 0
    ventas_miercoles_cafeteria = 0
    ventas_jueves_cafeteria = 0
    ventas_viernes_cafeteria = 0
    ventas_sabado_cafeteria = 0
    ventas_domingo_cafeteria = 0

    hoy = date.today()
    if hoy.weekday() == 0:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 0, 0,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0, 0,0,0)
    elif hoy.weekday() == 1:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 1,0,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0, 0,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,0,0,0)
    elif hoy.weekday() == 2:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 2,0,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0, 0,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 1,0,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_miercoles_libreria, ventas_miercoles_cafeteria = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        #ventas_miercoles_libreria, ventas_miercoles_cafeteria,ventas_miercoles_comercializadora = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,0,0,0)
    elif hoy.weekday() == 3:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 3,0,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0, 0,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 2,0,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_miercoles_libreria, ventas_miercoles_cafeteria = ventas_miercoles(hoy.day,hoy.month,hoy.year, 1,0,0,0)
        #ventas_miercoles_libreria, ventas_miercoles_cafeteria,ventas_miercoles_comercializadora = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_jueves_libreria, ventas_jueves_cafeteria = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        #ventas_jueves_libreria, ventas_jueves_cafeteria,ventas_jueves_comercializadora = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,0,0,0)
    elif hoy.weekday() == 4:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 4,0,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0, 0,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 3,0,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_miercoles_libreria, ventas_miercoles_cafeteria = ventas_miercoles(hoy.day,hoy.month,hoy.year, 2,0,0,0)
        #ventas_miercoles_libreria, ventas_miercoles_cafeteria,ventas_miercoles_comercializadora = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_jueves_libreria, ventas_jueves_cafeteria = ventas_jueves(hoy.day,hoy.month,hoy.year, 1,0,0,0)
        #ventas_jueves_libreria, ventas_jueves_cafeteria,ventas_jueves_comercializadora = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_viernes_libreria, ventas_viernes_cafeteria = ventas_viernes(hoy.day,hoy.month,hoy.year,0,0,0,0)
        #ventas_viernes_libreria, ventas_viernes_cafeteria,ventas_viernes_comercializadora = ventas_viernes(hoy.day,hoy.month,hoy.year,0,0,0,0)
    elif hoy.weekday() == 5:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 5,0,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0, 0,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 4,0,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_miercoles_libreria, ventas_miercoles_cafeteria = ventas_miercoles(hoy.day,hoy.month,hoy.year, 3,0,0,0)
        #ventas_miercoles_libreria, ventas_miercoles_cafeteria,ventas_miercoles_comercializadora = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_jueves_libreria, ventas_jueves_cafeteria = ventas_jueves(hoy.day,hoy.month,hoy.year, 2,0,0,0)
        #ventas_jueves_libreria, ventas_jueves_cafeteria,ventas_jueves_comercializadora = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_viernes_libreria, ventas_viernes_cafeteria = ventas_viernes(hoy.day,hoy.month,hoy.year,1,0,0,0)
        #ventas_viernes_libreria, ventas_viernes_cafeteria,ventas_viernes_comercializadora = ventas_viernes(hoy.day,hoy.month,hoy.year,0,0,0,0)
        ventas_sabado_libreria, ventas_sabado_cafeteria = ventas_sabado(hoy.day,hoy.month,hoy.year,0,0,0,0)
        #ventas_sabado_libreria, ventas_sabado_cafeteria,ventas_sabado_comercializadora = ventas_sabado(hoy.day,hoy.month,hoy.year,0,0,0,0)
    elif hoy.weekday() == 6:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year,6,0,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0, 0,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 5,0,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_miercoles_libreria, ventas_miercoles_cafeteria = ventas_miercoles(hoy.day,hoy.month,hoy.year, 4,0,0,0)
        #ventas_miercoles_libreria, ventas_miercoles_cafeteria,ventas_miercoles_comercializadora = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_jueves_libreria, ventas_jueves_cafeteria = ventas_jueves(hoy.day,hoy.month,hoy.year, 3,0,0,0)
        #ventas_jueves_libreria, ventas_jueves_cafeteria,ventas_jueves_comercializadora = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,0,0,0)
        ventas_viernes_libreria, ventas_viernes_cafeteria = ventas_viernes(hoy.day,hoy.month,hoy.year,2,0,0,0)
        #ventas_viernes_libreria, ventas_viernes_cafeteria,ventas_viernes_comercializadora = ventas_viernes(hoy.day,hoy.month,hoy.year,0,0,0,0)
        ventas_sabado_libreria, ventas_sabado_cafeteria = ventas_sabado(hoy.day,hoy.month,hoy.year,1,0,0,0)
        #ventas_sabado_libreria, ventas_sabado_cafeteria,ventas_sabado_comercializadora = ventas_sabado(hoy.day,hoy.month,hoy.year,0,0,0,0)
        ventas_domingo_libreria, ventas_domingo_cafeteria = ventas_domingo(hoy.day,hoy.month,hoy.year, 0,0 ,0,0)
        #ventas_domingo_libreria, ventas_domingo_cafeteria,ventas_domingo_comercializadora = ventas_domingo(hoy.day,hoy.month,hoy.year, 0,0 ,0,0)

    ventas_semana_libreria = ventas_domingo_libreria+ ventas_sabado_libreria+ventas_viernes_libreria+ventas_jueves_libreria+ventas_miercoles_libreria+ventas_martes_libreria+ventas_lunes_libreria
    ventas_semana_cafeteria = ventas_domingo_cafeteria + ventas_sabado_cafeteria + ventas_viernes_cafeteria + ventas_jueves_cafeteria + ventas_miercoles_cafeteria + ventas_martes_cafeteria + ventas_lunes_cafeteria
    #ventas_semana_comercializadora = ventas_domingo_comercializadora + ventas_sabado_comercializadora + ventas_viernes_comercializadora + ventas_jueves_comercializadora + ventas_miercoles_comercializadora + ventas_martes_comercializadora + ventas_lunes_comercializadora

    return ventas_semana_libreria, ventas_semana_cafeteria#,ventas_semana_comercializadora

def ventas_domingo(hoy,mes,anio,resta,usuario,validador,producto):
    if validador == 0:
        if usuario == 0:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_2 + Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_1 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()
            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()

        else:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_1 + Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_2 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()

            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
        return ventas_1, ventas_2#, ventas_sabado_comercializadorareturn ventas_viernes_libreria, ventas_viernes_cafeteria#,ventas_viernes_comercializadora
    elif validador == 1:
        if usuario == 0 and producto == 0:
            ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif usuario != 0:
            ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif producto != 0:
             ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,nombre_libro_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        return ventas_domingo_libreria
    elif validador == 2:
        if usuario == 0 and producto == 0:
            ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif usuario != 0:
            ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif producto != 0:
            ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,nombre_producto_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        return ventas_domingo_cafeteria
    """
    elif validador == 3:
        if usuario == 0 and producto == 0:
            ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif usuario != 0:
            ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif producto != 0:
             ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,nombre_articulo_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        return ventas_domingo_comercializadora
    """
def ventas_sabado(hoy,mes,anio,resta,usuario,validador,producto):
    if validador == 0:
        if usuario == 0:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_2 + Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_1 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()
            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()

        else:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_1 + Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_2 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()

            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
        return ventas_1, ventas_2#, ventas_sabado_comercializadorareturn ventas_viernes_libreria, ventas_viernes_cafeteria#,ventas_viernes_comercializadora
    elif validador == 1:
        if usuario == 0 and producto == 0:
            ventas_sabado_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif usuario != 0:
            ventas_sabado_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif producto != 0:
             ventas_sabado_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,nombre_libro_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        return ventas_sabado_libreria
    elif validador == 2:
        if usuario == 0 and producto == 0:
            ventas_sabado_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif usuario != 0:
            ventas_sabado_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif producto != 0:
            ventas_sabado_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,nombre_producto_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        return ventas_sabado_cafeteria
    """
    elif validador == 3:
        if usuario == 0 and producto == 0:
            ventas_sabado_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif usuario != 0:
            ventas_sabado_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif producto != 0:
             ventas_sabado_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,nombre_articulo_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        return ventas_sabado_comercializadora
    """
def ventas_viernes(hoy,mes,anio,resta,usuario,validador,producto):
    if validador == 0: #ambas
        if usuario == 0:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_2 + Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_1 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()
            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()

        else:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_1 + Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_2 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()

            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
        return ventas_1, ventas_2#, ventas_sabado_comercializadorareturn ventas_viernes_libreria, ventas_viernes_cafeteria#,ventas_viernes_comercializadora
    elif validador == 1: #libreria
        if usuario == 0 and producto == 0:
            ventas_viernes_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif usuario != 0:
            ventas_viernes_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif producto != 0:
             ventas_viernes_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,nombre_libro_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        return ventas_viernes_libreria
    elif validador == 2: #cafeteria
        if usuario == 0 and producto == 0:
            ventas_viernes_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif usuario != 0:
            ventas_viernes_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif producto != 0:
            ventas_viernes_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,nombre_producto_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        return ventas_viernes_cafeteria
    """
    elif validador == 3:
        if usuario == 0 and producto == 0:
            ventas_viernes_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif usuario != 0:
            ventas_viernes_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif producto != 0:
             ventas_viernes_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,nombre_articulo_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        return ventas_viernes_comercializadora
    """
def ventas_jueves(hoy,mes,anio,resta,usuario,validador,producto):
    if validador == 0:
        if usuario == 0:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_2 + Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_1 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()
            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()

        else:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_1 + Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_2 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()

            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
        return ventas_1, ventas_2#, ventas_sabado_comercializadorareturn ventas_viernes_libreria, ventas_viernes_cafeteria#,ventas_viernes_comercializadora
    elif validador == 1:
        if usuario == 0 and producto == 0:
            ventas_jueves_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif usuario != 0:
            ventas_jueves_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif producto != 0:
             ventas_jueves_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,nombre_libro_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        return ventas_jueves_libreria
    elif validador == 2:
        if usuario == 0 and producto == 0:
            ventas_jueves_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif usuario != 0:
            ventas_jueves_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif producto != 0:
            ventas_jueves_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,nombre_producto_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        return ventas_jueves_cafeteria
    """
    elif validador == 3:
        if usuario == 0 and producto == 0:
            ventas_jueves_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif usuario != 0:
            ventas_jueves_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif producto != 0:
             ventas_jueves_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,nombre_articulo_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        return ventas_jueves_comercializadora
    """
def ventas_miercoles(hoy,mes,anio,resta,usuario,validador,producto):
    if validador == 0:
        if usuario == 0:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_2 + Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_1 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()
            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()

        else:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_1 + Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_2 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()

            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
        return ventas_1, ventas_2#, ventas_sabado_comercializadorareturn ventas_viernes_libreria, ventas_viernes_cafeteria#,ventas_viernes_comercializadora
    elif validador == 1:
        if usuario == 0 and producto == 0:
            ventas_miercoles_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif usuario != 0:
            ventas_miercoles_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif producto != 0:
             ventas_miercoles_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,nombre_libro_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        return ventas_miercoles_libreria
    elif validador == 2:
        if usuario == 0 and producto == 0:
            ventas_miercoles_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif usuario != 0:
            ventas_miercoles_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif producto != 0:
            ventas_miercoles_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,nombre_producto_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        return ventas_miercoles_cafeteria
    """
    elif validador == 3:
        if usuario == 0 and producto == 0:
            ventas_miercoles_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif usuario != 0:
            ventas_miercoles_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif producto != 0:
             ventas_miercoles_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,nombre_articulo_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        return ventas_miercoles_comercializadora
    """
def ventas_martes(hoy,mes,anio,resta,usuario,validador,producto):
    if validador == 0:
        if usuario == 0:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_2 + Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_1 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()
            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()

        else:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_1 + Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_2 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()

            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
        return ventas_1, ventas_2#, ventas_sabado_comercializadorareturn ventas_viernes_libreria, ventas_viernes_cafeteria#,ventas_viernes_comercializadora
    elif validador == 1:
        if usuario == 0 and producto == 0:
            ventas_martes_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif usuario != 0:
            ventas_martes_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif producto != 0:
             ventas_martes_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,nombre_libro_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        return ventas_martes_libreria
    elif validador == 2:
        if usuario == 0 and producto == 0:
            ventas_martes_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif usuario != 0:
            ventas_martes_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif producto != 0:
            ventas_martes_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,nombre_producto_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        return ventas_martes_cafeteria
    """
    elif validador == 3:
        if usuario == 0 and producto == 0:
            ventas_martes_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif usuario != 0:
            ventas_martes_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif producto != 0:
             ventas_martes_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,nombre_articulo_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        return ventas_martes_comercializadora
    """

def ventas_lunes(hoy,mes,anio,resta,usuario,validador,producto):
    if validador == 0:
        if usuario == 0:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_2 + Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_1 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()
            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).count()

        else:
            articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
            articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
            ventas_1 = 0
            ventas_2 = 0
            for articulo_libreria in articulos_libreria:
                ventas_1 = ventas_1 + Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_libro = int(articulo_libreria.id)).count()
            for articulo_cafeteria in articulos_cafeteria:
                ventas_2 = ventas_2 + productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_por=usuario, vendido_el_mes = mes,vendido_el_anio = anio,nombre_producto = int(articulo_cafeteria.id)).count()

            #ventas_domingo_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
            #ventas_domingo_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).count()
        return ventas_1, ventas_2#, ventas_sabado_comercializadorareturn ventas_viernes_libreria, ventas_viernes_cafeteria#,ventas_viernes_comercializadora
    elif validador == 1:
        if usuario == 0 and producto == 0:
            ventas_lunes_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif usuario != 0:
            ventas_lunes_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        elif producto != 0:
            ventas_lunes_libreria = Producto.objects.all().filter(vendido_el_dia = hoy-resta,nombre_libro_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_libro').distinct()
        return ventas_lunes_libreria
    elif validador == 2:
        if usuario == 0 and producto == 0:
            ventas_lunes_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif usuario != 0:
            ventas_lunes_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        elif producto != 0:
            ventas_lunes_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy-resta,nombre_producto_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_producto').distinct()
        return ventas_lunes_cafeteria
    """
    elif validador == 3:
        if usuario == 0 and producto == 0:
            ventas_lunes_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif usuario != 0:
            ventas_lunes_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,vendido_por = usuario, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        elif producto != 0:
             ventas_lunes_comercializadora = Producto_comercializadora.objects.all().filter(vendido_el_dia = hoy-resta,nombre_articulo_id = producto, vendido_el_mes = mes,vendido_el_anio = anio).values('nombre_articulo').distinct()
        return ventas_lunes_comercializadora
    """

def ventas_semana_ven(usuario):
    ventas_lunes_libreria= 0
    ventas_martes_libreria = 0
    ventas_miercoles_libreria = 0
    ventas_jueves_libreria = 0
    ventas_viernes_libreria = 0
    ventas_sabado_libreria = 0
    ventas_domingo_libreria = 0

    ventas_lunes_comercializadora= 0
    ventas_martes_comercializadora = 0
    ventas_miercoles_comercializadora = 0
    ventas_jueves_comercializadora = 0
    ventas_viernes_comercializadora = 0
    ventas_sabado_comercializadora = 0
    ventas_domingo_comercializadora = 0

    ventas_lunes_cafeteria = 0
    ventas_martes_cafeteria = 0
    ventas_miercoles_cafeteria = 0
    ventas_jueves_cafeteria = 0
    ventas_viernes_cafeteria = 0
    ventas_sabado_cafeteria = 0
    ventas_domingo_cafeteria = 0

    hoy = date.today()
    if hoy.weekday() == 0:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
    elif hoy.weekday() == 1:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 1,usuario,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
    elif hoy.weekday() == 2:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 2,usuario,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 1,usuario,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_miercoles_libreria, ventas_miercoles_cafeteria = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        #ventas_miercoles_libreria, ventas_miercoles_cafeteria,ventas_miercoles_comercializadora = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
    elif hoy.weekday() == 3:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 3,usuario,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 2,usuario,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_miercoles_libreria, ventas_miercoles_cafeteria = ventas_miercoles(hoy.day,hoy.month,hoy.year, 1,usuario,0,0)
        #ventas_miercoles_libreria, ventas_miercoles_cafeteria,ventas_miercoles_comercializadora = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_jueves_libreria, ventas_jueves_cafeteria = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        #ventas_jueves_libreria, ventas_jueves_cafeteria,ventas_jueves_comercializadora = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
    elif hoy.weekday() == 4:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 4,usuario,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 3,usuario,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_miercoles_libreria, ventas_miercoles_cafeteria = ventas_miercoles(hoy.day,hoy.month,hoy.year, 2,usuario,0,0)
        #ventas_miercoles_libreria, ventas_miercoles_cafeteria,ventas_miercoles_comercializadora = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_jueves_libreria, ventas_jueves_cafeteria = ventas_jueves(hoy.day,hoy.month,hoy.year, 1,usuario,0,0)
        #ventas_jueves_libreria, ventas_jueves_cafeteria,ventas_jueves_comercializadora = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_viernes_libreria, ventas_viernes_cafeteria = ventas_viernes(hoy.day,hoy.month,hoy.year,0,usuario,0,0)
        #ventas_viernes_libreria, ventas_viernes_cafeteria,ventas_viernes_comercializadora = ventas_viernes(hoy.day,hoy.month,hoy.year,0,usuario,0,0)
    elif hoy.weekday() == 5:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 5,usuario,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 4,usuario,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_miercoles_libreria, ventas_miercoles_cafeteria = ventas_miercoles(hoy.day,hoy.year,hoy.month, 3,usuario,0,0)
        #ventas_miercoles_libreria, ventas_miercoles_cafeteria,ventas_miercoles_comercializadora = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_jueves_libreria, ventas_jueves_cafeteria = ventas_jueves(hoy.day,hoy.month,hoy.year, 2,usuario,0,0)
        #ventas_jueves_libreria, ventas_jueves_cafeteria,ventas_jueves_comercializadora = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_viernes_libreria, ventas_viernes_cafeteria = ventas_viernes(hoy.day,hoy.month,hoy.year,1,usuario,0,0)
        #ventas_viernes_libreria, ventas_viernes_cafeteria,ventas_viernes_comercializadora = ventas_viernes(hoy.day,hoy.month,hoy.year,0,usuario,0,0)
        ventas_sabado_libreria, ventas_sabado_cafeteria = ventas_sabado(hoy.day,hoy.month,hoy.year,0,usuario,0,0)
        #ventas_sabado_libreria, ventas_sabado_cafeteria,ventas_sabado_comercializadora = ventas_sabado(hoy.day,hoy.month,hoy.year,0,usuario,0,0)
    elif hoy.weekday() == 6:
        ventas_lunes_libreria, ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 6,usuario,0,0)
        #ventas_lunes_libreria, ventas_lunes_cafeteria,ventas_lunes_comercializadora = ventas_lunes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_martes_libreria, ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 5,usuario,0,0)
        #ventas_martes_libreria, ventas_martes_cafeteria,ventas_martes_comercializadora = ventas_martes(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_miercoles_libreria, ventas_miercoles_cafeteria = ventas_miercoles(hoy.day,hoy.month,hoy.year, 4,usuario,0,0)
        #ventas_miercoles_libreria, ventas_miercoles_cafeteria,ventas_miercoles_comercializadora = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_jueves_libreria, ventas_jueves_cafeteria = ventas_jueves(hoy.day,hoy.month,hoy.year, 3,usuario,0,0)
        #ventas_jueves_libreria, ventas_jueves_cafeteria,ventas_jueves_comercializadora = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        ventas_viernes_libreria, ventas_viernes_cafeteria = ventas_viernes(hoy.day,hoy.month,hoy.year,2,usuario,0,0)
        #ventas_viernes_libreria, ventas_viernes_cafeteria,ventas_viernes_comercializadora = ventas_viernes(hoy.day,hoy.month,hoy.year,0,usuario,0,0)
        ventas_sabado_libreria, ventas_sabado_cafeteria = ventas_sabado(hoy.day,hoy.month,hoy.year,1,usuario,0,0)
        #ventas_sabado_libreria, ventas_sabado_cafeteria,ventas_sabado_comercializadora = ventas_sabado(hoy.day,hoy.month,hoy.year,0,usuario,0,0)
        ventas_domingo_libreria, ventas_domingo_cafeteria = ventas_domingo(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)
        #ventas_domingo_libreria, ventas_domingo_cafeteria,ventas_domingo_comercializadora = ventas_domingo(hoy.day,hoy.month,hoy.year, 0,usuario,0,0)

    ventas_semana_libreria = ventas_domingo_libreria+ ventas_sabado_libreria+ventas_viernes_libreria+ventas_jueves_libreria+ventas_miercoles_libreria+ventas_martes_libreria+ventas_lunes_libreria
    ventas_semana_cafeteria = ventas_domingo_cafeteria + ventas_sabado_cafeteria + ventas_viernes_cafeteria + ventas_jueves_cafeteria + ventas_miercoles_cafeteria + ventas_martes_cafeteria + ventas_lunes_cafeteria
    #ventas_semana_comercializadora = ventas_domingo_comercializadora + ventas_sabado_comercializadora + ventas_viernes_comercializadora + ventas_jueves_comercializadora + ventas_miercoles_comercializadora + ventas_martes_comercializadora + ventas_lunes_comercializadora

    return ventas_semana_libreria, ventas_semana_cafeteria#,ventas_semana_comercializadora

def ventas_semana_libreria_inicial(usuario,producto):
    dict = []
    hoy = date.today()
    if hoy.weekday() == 0:
        ventas_lunes_libreria = ventas_lunes(hoy.day,hoy.month,hoy.year, 0, usuario,1,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)

    elif hoy.weekday() == 1:
        ventas_lunes_libreria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 1,usuario,1,producto)
        ventas_martes_libreria = ventas_martes(hoy.day,hoy.month,hoy.year, 0,usuario,1,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 2:
        ventas_lunes_libreria = ventas_lunes(hoy.day,hoy.month,hoy.year, 2,usuario,1,producto)
        ventas_martes_libreria = ventas_martes(hoy.day,hoy.month,hoy.year, 1,usuario,1,producto)
        ventas_miercoles_libreria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,usuario,1,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 3:
        ventas_lunes_libreria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 3,usuario,1,producto)
        ventas_martes_libreria  = ventas_martes(hoy.day,hoy.month,hoy.year, 2,usuario,1,producto)
        ventas_miercoles_libreria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 1,usuario,1,producto)
        ventas_jueves_libreria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,usuario,1,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_libreria:
            pro = Articulo_libreria.objects.all.filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 4:
        ventas_lunes_libreria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 4,usuario,1,producto)
        ventas_martes_libreria  = ventas_martes(hoy.day,hoy.month,hoy.year, 3,usuario,1,producto)
        ventas_miercoles_libreria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 2,usuario,1,producto)
        ventas_jueves_libreria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 1,usuario,1,producto)
        ventas_viernes_libreria  = ventas_viernes(hoy.day,hoy.month,hoy.year,0,usuario,1,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
        for libro in ventas_viernes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'viernes'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 5:
        ventas_lunes_libreria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 5,usuario,1,producto)
        ventas_martes_libreria  = ventas_martes(hoy.day,hoy.month,hoy.year, 4,usuario,1,producto)
        ventas_miercoles_libreria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 3,usuario,1,producto)
        ventas_jueves_libreria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 2,usuario,1,producto)
        ventas_viernes_libreria  = ventas_viernes(hoy.day,hoy.month,hoy.year,1,usuario,1,producto)
        ventas_sabado_libreria = ventas_sabado(hoy.day,hoy.month,hoy.year,0,usuario,1,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
        for libro in ventas_viernes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'viernes'
                }
                dict.append(dict_dict)
        for libro in ventas_sabado_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'sabado'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 6:
        ventas_lunes_libreria = ventas_lunes(hoy.day,hoy.month,hoy.year,6,usuario,1,producto)
        ventas_martes_libreria  = ventas_martes(hoy.day,hoy.month,hoy.year, 5,usuario,1,producto)
        ventas_miercoles_libreria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 4,usuario,1,producto)
        ventas_jueves_libreria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 3,usuario,1,producto)
        ventas_viernes_libreria  = ventas_viernes(hoy.day,hoy.month,hoy.year,2,usuario,1,producto)
        ventas_sabado_libreria  = ventas_sabado(hoy.day,hoy.month,hoy.year,1,usuario,1,producto)
        ventas_domingo_libreria  = ventas_domingo(hoy.day,hoy.month,hoy.year, 0,usuario,1,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-6,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-6,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
        for libro in ventas_viernes_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'viernes'
                }
                dict.append(dict_dict)
        for libro in ventas_sabado_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'sabado'
                }
                dict.append(dict_dict)
        for libro in ventas_domingo_libreria:
            pro = Articulo_libreria.objects.all().filter(sucursal=1).filter(id = int(libro['nombre_libro']))
            product = Producto.objects.all().filter(nombre_libro_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'domingo'
                }
                dict.append(dict_dict)
    return dict






def ventas_semana_cafeteria_inicial(usuario,producto):
    dict = []
    hoy = date.today()
    if hoy.weekday() == 0:
        ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 0, usuario,2,producto)
        for libro in ventas_lunes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 1:
        ventas_lunes_cafeteria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 1,usuario,2,producto)
        ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 0,usuario,2,producto)
        for libro in ventas_lunes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 2:
        ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year, 2,usuario,2,producto)
        ventas_martes_cafeteria = ventas_martes(hoy.day,hoy.month,hoy.year, 1,usuario,2,producto)
        ventas_miercoles_cafeteria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,usuario,2,producto)
        for libro in ventas_lunes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 3:
        ventas_lunes_cafeteria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 3,usuario,2,producto)
        ventas_martes_cafeteria  = ventas_martes(hoy.day,hoy.month,hoy.year, 2,usuario,2,producto)
        ventas_miercoles_cafeteria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 1,usuario,2,producto)
        ventas_jueves_cafeteria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,usuario,2,producto)
        for libro in ventas_lunes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 4:
        ventas_lunes_cafeteria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 4,usuario,2,producto)
        ventas_martes_cafeteria  = ventas_martes(hoy.day,hoy.month,hoy.year, 3,usuario,2,producto)
        ventas_miercoles_cafeteria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 2,usuario,2,producto)
        ventas_jueves_cafeteria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 1,usuario,2,producto)
        ventas_viernes_cafeteria  = ventas_viernes(hoy.day,hoy.month,hoy.year,0,usuario,2,producto)
        for libro in ventas_lunes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)

        for libro in ventas_miercoles_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
        for libro in ventas_viernes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'viernes'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 5:
        ventas_lunes_cafeteria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 5,usuario,2,producto)
        ventas_martes_cafeteria  = ventas_martes(hoy.day,hoy.month,hoy.year, 4,usuario,2,producto)
        ventas_miercoles_cafeteria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 3,usuario,2,producto)
        ventas_jueves_cafeteria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 2,usuario,2,producto)
        ventas_viernes_cafeteria  = ventas_viernes(hoy.day,hoy.month,hoy.year,1,usuario,2,producto)
        ventas_sabado_cafeteria = ventas_sabado(hoy.day,hoy.month,hoy.year,0,usuario,2,producto)
        for libro in ventas_lunes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
        for libro in ventas_viernes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'viernes'
                }
                dict.append(dict_dict)
        for libro in ventas_sabado_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'sabado'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 6:
        ventas_lunes_cafeteria = ventas_lunes(hoy.day,hoy.month,hoy.year,6,usuario,2,producto)
        ventas_martes_cafeteria  = ventas_martes(hoy.day,hoy.month,hoy.year, 5,usuario,2,producto)
        ventas_miercoles_cafeteria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 4,usuario,2,producto)
        ventas_jueves_cafeteria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 3,usuario,2,producto)
        ventas_viernes_cafeteria  = ventas_viernes(hoy.day,hoy.month,hoy.year,2,usuario,2,producto)
        ventas_sabado_cafeteria  = ventas_sabado(hoy.day,hoy.month,hoy.year,1,usuario,2,producto)
        ventas_domingo_cafeteria  = ventas_domingo(hoy.day,hoy.month,hoy.year, 0,usuario,2,producto)
        for libro in ventas_lunes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-6,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-6,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
        for libro in ventas_viernes_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'viernes'
                }
                dict.append(dict_dict)
        for libro in ventas_sabado_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'sabado'
                }
                dict.append(dict_dict)
        for libro in ventas_domingo_cafeteria:
            pro = Articulo_cafeteria.objects.all(sucursal=1).filter(id = int(libro['nombre_producto']))
            product = productos.objects.all().filter(nombre_producto_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'domingo'
                }
                dict.append(dict_dict)
    return dict




"""

def ventas_semana_comercializadora_inicial(usuario,producto):
    dict = []
    hoy = date.today()
    if hoy.weekday() == 0:
        ventas_lunes_libreria = ventas_lunes(hoy.day,hoy.month,hoy.year, 0, usuario,3,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)

    elif hoy.weekday() == 1:
        ventas_lunes_libreria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 1,usuario,3,producto)
        ventas_martes_libreria = ventas_martes(hoy.day,hoy.month,hoy.year, 0,usuario,3,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 2:
        ventas_lunes_libreria = ventas_lunes(hoy.day,hoy.month,hoy.year, 2,usuario,3,producto)
        ventas_martes_libreria = ventas_martes(hoy.day,hoy.month,hoy.year, 1,usuario,3,producto)
        ventas_miercoles_libreria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 0,usuario,3,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 3:
        ventas_lunes_libreria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 3,usuario,3,producto)
        ventas_martes_libreria  = ventas_martes(hoy.day,hoy.month,hoy.year, 2,usuario,3,producto)
        ventas_miercoles_libreria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 1,usuario,3,producto)
        ventas_jueves_libreria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 0,usuario,3,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 4:
        ventas_lunes_libreria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 4,usuario,3,producto)
        ventas_martes_libreria  = ventas_martes(hoy.day,hoy.month,hoy.year, 3,usuario,3,producto)
        ventas_miercoles_libreria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 2,usuario,3,producto)
        ventas_jueves_libreria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 1,usuario,3,producto)
        ventas_viernes_libreria  = ventas_viernes(hoy.day,hoy.month,hoy.year,0,usuario,3,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
        for libro in ventas_viernes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'viernes'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 5:
        ventas_lunes_libreria  = ventas_lunes(hoy.day,hoy.month,hoy.year, 5,usuario,3,producto)
        ventas_martes_libreria  = ventas_martes(hoy.day,hoy.month,hoy.year, 4,usuario,3,producto)
        ventas_miercoles_libreria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 3,usuario,3,producto)
        ventas_jueves_libreria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 2,usuario,3,producto)
        ventas_viernes_libreria  = ventas_viernes(hoy.day,hoy.month,hoy.year,1,usuario,3,producto)
        ventas_sabado_libreria = ventas_sabado(hoy.day,hoy.month,hoy.year,0,usuario,3,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
        for libro in ventas_viernes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'viernes'
                }
                dict.append(dict_dict)
        for libro in ventas_sabado_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'sabado'
                }
                dict.append(dict_dict)
    elif hoy.weekday() == 6:
        ventas_lunes_libreria = ventas_lunes(hoy.day,hoy.month,hoy.year,6,usuario,3,producto)
        ventas_martes_libreria  = ventas_martes(hoy.day,hoy.month,hoy.year, 5,usuario,3,producto)
        ventas_miercoles_libreria  = ventas_miercoles(hoy.day,hoy.month,hoy.year, 4,usuario,3,producto)
        ventas_jueves_libreria  = ventas_jueves(hoy.day,hoy.month,hoy.year, 3,usuario,3,producto)
        ventas_viernes_libreria  = ventas_viernes(hoy.day,hoy.month,hoy.year,2,usuario,3,producto)
        ventas_sabado_libreria  = ventas_sabado(hoy.day,hoy.month,hoy.year,1,usuario,3,producto)
        ventas_domingo_libreria  = ventas_domingo(hoy.day,hoy.month,hoy.year, 0,usuario,3,producto)
        for libro in ventas_lunes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-6,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-6,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'lunes'
                }
                dict.append(dict_dict)
        for libro in ventas_martes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-5,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'martes'
                }
                dict.append(dict_dict)
        for libro in ventas_miercoles_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-4,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'miercoles'
                }
                dict.append(dict_dict)
        for libro in ventas_jueves_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-3,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'jueves'
                }
                dict.append(dict_dict)
        for libro in ventas_viernes_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Articulo_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-2,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'viernes'
                }
                dict.append(dict_dict)
        for libro in ventas_sabado_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-1,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'sabado'
                }
                dict.append(dict_dict)
        for libro in ventas_domingo_libreria:
            pro = Articulo_comercializadora.objects.all().filter(id = int(libro['nombre_articulo']))
            product = Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id))
            if(len(pro) != 0 and len(product) != 0):
                dict_dict = {
                    'nombre' : str(pro[0]),
                    'vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(pro[0].id), vendido = 1,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo = int(pro[0].id), vendido = 0,vendido_el_dia = hoy.day-0,vendido_el_anio = hoy.year, vendido_el_mes = hoy.month).count()),
                    'precio': str(product[0].precio),
                    'costo': str(product[0].costo),
                    'codigo_barras': str(product[0].codigo_barras),
                    'dia':'domingo'
                }
                dict.append(dict_dict)
    return dict
"""