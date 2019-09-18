# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from registro.models import UserProfile
from cafeteria_puebla.forms import productosForm, ArticuloForm, Cambiar_precio_form, borrar_producto_form
from datetime import date
from cafeteria.models import productos, Articulo
from django.contrib.auth.decorators import login_required
import json

@login_required
def inicio(request):
    dict_context = {}
    profileuser = UserProfile.objects.get(user = request.user)
    dict_context['profileuser'] = profileuser
    return render(request,'cafeteria_puebla/cafeteria_inicio.html' ,dict_context)
@login_required
def agregar_producto(request):
    dict_context = {}
    if request.method == 'POST':
        agregar_form = productosForm(data= request.POST)
        if agregar_form.is_valid():
            i = 0
            try:
                j = productos.objects.all().order_by('-id')[0]
                j = j.id+1
            except:
                j = 0
            while(i< int(request.POST.get('numero_productos'))):
                producto = agregar_form.save(commit = False)
                dia = date.today()
                producto.agregado_el_anio = dia.year
                producto.agregado_el_mes = dia.month
                producto.agregado_el_dia = dia.day
                producto.codigo_barras = request.POST.get('codigo_barras')
                producto.precio = request.POST.get('precio')
                producto.id = j
                producto.save()
                i = i+1
                j = j+1
            dict_context['articulo_form'] = ArticuloForm()
            dict_context['agregar_form'] = productosForm()
            dict_context['validador'] = 1
            dict_context['usuario'] = UserProfile.objects.get(user = request.user)
            return render(request, 'cafeteria_puebla/agregarproducto.html', dict_context)
        else:
            dict_context['articulo_form'] = ArticuloForm()
            dict_context['validador'] = 0
            dict_context['agregar_form'] = agregar_form
            dict_context['usuario'] = UserProfile.objects.get(user = request.user)
            return render(request, 'cafeteria_puebla/agregarproducto.html', dict_context)
    agregar_form = productosForm()
    dict_context['usuario'] = UserProfile.objects.get(user = request.user)
    dict_context['articulo_form'] = ArticuloForm()
    dict_context['agregar_form'] = agregar_form
    dict_context['validador'] = 0
    return render(request, 'cafeteria_puebla/agregarproducto.html', dict_context)

@login_required
def agregar_articulo(request):
    context_dict = {}
    if request.method == 'POST':
        articulo_form = ArticuloForm(request.POST)
        if articulo_form.is_valid():
            articulo_nuevo = articulo_form.save(commit=False)
            articulo_nuevo.sucursal = 1
            articulo_nuevo.save()
            context_dict['articulo_form'] = ArticuloForm()
            context_dict['validador'] = 1
            context_dict['agregar_form'] = productosForm()
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
            return render(request, 'cafeteria_puebla/agregarproducto.html', context_dict)
        else:
            context_dict['articulo_form'] = articulo_form
            context_dict['validador'] = 0
            context_dict['agregar_form'] = productosForm()
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
            return render(request, 'cafeteria_puebla/agregarproducto.html', context_dict)
    context_dict['articulo_form'] = ArticuloForm()
    context_dict['validador'] = 0
    context_dict['agregar_form'] = productosForm()
    context_dict['usuario'] = UserProfile.objects.get(user = request.user)
    return render(request, 'cafeteria_puebla/agregarproducto.html', context_dict)

@login_required
def busqueda(request):
    if request.method == 'GET':
        codigo = request.GET['codigo']
        producto = productos.objects.all().filter(codigo_barras=codigo,sucursal=1)
        if producto:
            return HttpResponse(1)
@login_required
def caja_registradora(request):
    context_dict = {}
    context_dict['validador'] = 0
    context_dict['usuario'] = UserProfile.objects.get(user = request.user)
    return render(request,'cafeteria_puebla/caja_registradora.html', context_dict)
@login_required
def muestro_producto(request, producto_slug):
    context_dict = {}
    try:
        producto = Articulo.objects.get(slug = producto_slug)
        context_dict['titulo'] = producto
        dict = []
        pro = productos.objects.all().filter(nombre_producto = producto)
        if (len(pro) != 0):
            dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(productos.objects.all().filter(nombre_producto_id = int(producto.id), vendido = 1).count()),
                        'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(producto.id),vendido = 0).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
                        'codigo_barras': str(pro[0].codigo_barras)
            }
            dict.append(dict_dict)
            context_dict['productos'] = dict
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
    except producto.DoesNotExist:
        context_dict['usuario'] = UserProfile.objects.get(user = request.user)
    return render(request,'cafeteria_puebla/busqueda_producto.html',context_dict)

@login_required
def ventas_caja(request):
    if request.method == 'GET':
        id_producto = request.GET['codigo']
        validador = request.GET['cancelado']
        salvar = productos.objects.get(id = id_producto)
        nombre = Articulo.objects.get(id = salvar.nombre_producto_id)
        if int(validador) == 0:
            salvar.vendido = 1
            salvar.vendido_por = request.user
            dia = date.today()
            salvar.vendido_el_anio = dia.year
            salvar.vendido_el_mes = dia.month
            salvar.vendido_el_dia = dia.day
        elif int(validador) == 1:
            salvar.vendido = 0
        salvar.en_caja = 0
        salvar.save()
        return HttpResponse(json.dumps({'nombre':nombre.nombre}),content_type = 'aplication/json')
@login_required
def cambiar_precio_producto(request):
    context_dict = {}
    if request.method == 'POST':
        precio_form = Cambiar_precio_form(request.POST)
        if precio_form.is_valid():
            busqueda = productos.objects.all().filter(nombre_producto_id = request.POST.get('producto')).exclude(vendido = 1)
            for producto in busqueda:
                producto.precio = request.POST.get('precio')
                producto.save()
            context_dict['validador'] = 2
            context_dict['precio_form'] = Cambiar_precio_form()
            context_dict['cafeteria_val'] = 1
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
            return render(request,'libreria_puebla/cambiar_precio_libro.html', context_dict)
        else:
            context_dict['cafeteria_val'] = 1
            context_dict['validador'] = 0
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
            context_dict['precio_form'] = precio_form
            return render(request, 'libreria_puebla/cambiar_precio_libro.html', context_dict)
    context_dict['cafeteria_val'] = 1
    context_dict['validador'] = 0
    context_dict['precio_form'] = Cambiar_precio_form()
    context_dict['usuario'] = UserProfile.objects.get(user = request.user)
    return render(request, 'libreria_puebla/cambiar_precio_libro.html', context_dict)
@login_required
def borrar_producto(request):
    context_dict = {}
    if request.method == 'POST':
        borrar_form = borrar_producto_form(request.POST)
        if borrar_form.is_valid():
            borrar = productos.objects.all().filter(nombre_producto_id = int(request.POST.get('producto')), vendido = 0)
            for b in borrar:
                b.delete()
        context_dict['usuario'] = UserProfile.objects.get(user = request.user)
        context_dict['validador'] = 4
        context_dict['borrar_form'] = borrar_producto_form()
    else:
        context_dict['usuario'] = UserProfile.objects.get(user = request.user)
        context_dict['validador'] = 0
        context_dict['borrar_form'] = borrar_producto_form()
    return render(request,'cafeteria_puebla/borrar_producto.html', context_dict)

def imprimir(request):
    return render(request, 'cafeteria_puebla/probando_imprimir.html')
