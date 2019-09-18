from django.shortcuts import render
from django.contrib.auth.models import User
from cafeteria.models import productos,Articulo as Articulo_cafeteria
from libreria.models import Producto, Articulo as Articulo_libreria
from comercializadora.models import Producto_comercializadora as PC
from datetime import date
from control_puebla.ventas_semana import ventas_semana
from control_puebla.forms import form_user, form_libro, form_cafeteria, form_user_cafeteria#, form_comercializadora
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    context_dict = {}
    hoy = date.today()
    articulos_libreria = Articulo_libreria.objects.all().filter(sucursal = 1)
    articulos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
    ventas_hoy_libreria=0
    ventas_hoy_cafeteria=0
    for articulo_libreria in articulos_libreria:
        ventas_hoy_libreria = ventas_hoy_libreria + Producto.objects.all().filter(vendido_el_dia = hoy.day,vendido_el_mes = hoy.month, vendido_el_anio = hoy.year,nombre_libro = int(articulo_libreria.id)).count()
    for articulo_cafeteria in articulos_cafeteria:
        ventas_hoy_cafeteria = ventas_hoy_cafeteria + productos.objects.all().filter(vendido_el_dia = hoy.day,vendido_el_mes = hoy.month, vendido_el_anio = hoy.year,nombre_producto = int(articulo_cafeteria.id)).count()

    #ventas_hoy_libreria = Producto.objects.all().filter(vendido_el_dia = hoy.day,vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()
    #ventar_hoy_cafeteria = productos.objects.all().filter(vendido_el_dia = hoy.day,vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()
    ventas_hoy_comercializadora = 0#PC.objects.all().filter(vendido_el_dia = hoy.day,vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()
    context_dict['ventas_semana_libreria'],context_dict['ventas_semana_cafeteria'] = ventas_semana()
    ventas_mes_libreria=0
    ventas_mes_cafeteria=0
    for articulo_libreria in articulos_libreria:
        ventas_mes_libreria = ventas_mes_libreria + Producto.objects.all().filter(vendido_el_mes = hoy.month, vendido_el_anio = hoy.year,nombre_libro = int(articulo_libreria.id)).count()
    for articulo_cafeteria in articulos_cafeteria:
        ventas_mes_cafeteria = ventas_mes_cafeteria + productos.objects.all().filter(vendido_el_mes = hoy.month, vendido_el_anio = hoy.year,nombre_producto = int(articulo_cafeteria.id)).count()


    context_dict['ventas_mes_libreria'] = ventas_mes_libreria
    context_dict['ventas_mes_cafeteria'] =ventas_mes_cafeteria
    context_dict['ventas_mes_comercializadora'] = 0#PC.objects.all().filter(vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()

    context_dict['ventas_hoy_libreria'] = ventas_hoy_libreria
    context_dict['ventas_hoy_cafeteria'] = ventas_hoy_cafeteria
    context_dict['ventas_hoy_comercializadora'] = ventas_hoy_comercializadora

    return render(request, 'control_puebla/inicio.html', context_dict)
@login_required
def ventas_dia_libreria(request):
    context_dict = {}
    context_dict['form_user'] = form_user()
    context_dict['libro_form'] = form_libro()
    return render(request, 'control_puebla/ventas_dia.html', context_dict)
@login_required
def ventas_semana_libreria(request):
    context_dict = {}
    context_dict['form_user'] = form_user()
    context_dict['libro_form'] = form_libro()
    return render(request, 'control_puebla/ventas_semana.html', context_dict)
@login_required
def ventas_mes_libreria(request):
    context_dict = {}
    context_dict['form_user'] = form_user()
    context_dict['libro_form'] = form_libro()
    return render(request, 'control_puebla/ventas_mes.html', context_dict)
"""
def ventas_dia_comercializadora(request):
    context_dict = {}
    context_dict['form_user'] = form_user()
    context_dict['libro_form'] = form_comercializadora()
    return render(request, 'control_puebla/ventas_dia_comercializadora.html', context_dict)

@login_required
def ventas_semana_comercializadora(request):
    context_dict = {}
    context_dict['form_user'] = form_user()
    context_dict['libro_form'] = form_comercializadora()
    return render(request, 'control_puebla/ventas_semana_comercializadora.html', context_dict)
@login_required
def ventas_mes_comercializadora(request):
    context_dict = {}
    context_dict['form_user'] = form_user()
    context_dict['libro_form'] = form_comercializadora()
    return render(request, 'control_puebla/ventas_mes_comercializadora.html', context_dict)
"""
@login_required
def ventas_dia_cafeteria(request):
    context_dict = {}
    context_dict['form_user'] = form_user_cafeteria()
    context_dict['cafeteria_form'] = form_cafeteria()
    return render(request, 'control_puebla/ventas_dia_cafeteria.html', context_dict)
@login_required
def ventas_semana_cafeteria(request):
    context_dict = {}
    context_dict['form_user'] = form_user_cafeteria()
    context_dict['cafeteria_form'] = form_cafeteria()
    return render(request, 'control_puebla/ventas_semana_cafeteria.html', context_dict)
@login_required
def ventas_mes_cafeteria(request):
    context_dict = {}
    context_dict['form_user'] = form_user_cafeteria()
    context_dict['cafeteria_form'] = form_cafeteria()
    return render(request, 'control_puebla/ventas_mes_cafeteria.html', context_dict)
@login_required
def libros_registrados(request):
    context_dict = {}
    context_dict['libro_form'] = form_libro()
    return render(request, 'control_puebla/libros_registrados.html', context_dict)
"""
@login_required
def articulos_registrados(request):
    context_dict = {}
    context_dict['libro_form'] = form_comercializadora()
    return render(request, 'control/articulos_registrados.html', context_dict)
"""
@login_required
def productos_registrados(request):
    context_dict = {}
    context_dict['cafeteria_form'] = form_cafeteria()
    return render(request, 'control_puebla/productos_registrados.html', context_dict)

