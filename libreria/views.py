# -*- coding: utf-8 -*-

from django.shortcuts import render
from registro.models import UserProfile
from libreria.forms import CategoriaForm, ProductoForm,ArticuloForm, Cambiar_precio_form,borrar_libro_form
from libreria.models import Producto, Categoria, Articulo
from datetime import date
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse

@login_required
def inicio(request):
    dict_context = {}
    profileuser = UserProfile.objects.get(user = request.user)
    dict_context['profileuser'] = profileuser
    return render(request,'libreria/libreria_inicio.html' ,dict_context)

@login_required
def agregar_categoria(request):
    dict_context = {}
    if request.method == 'POST':
        categoria_form = CategoriaForm(data = request.POST)
        if categoria_form.is_valid():
            categoria_form.save()
            dict_context['usuario'] = UserProfile.objects.get(user = request.user)
            dict_context['validador'] = 1
            dict_context['categoria_form'] = CategoriaForm()
            return render(request, 'libreria/agregar_categoria.html', dict_context)
        else:
            dict_context['validador']=0
            dict_context['categoria_form'] = categoria_form
            dict_context['usuario'] = UserProfile.objects.get(user = request.user)
            return render(request, 'libreria/agregar_categoria.html',dict_context)
    dict_context['usuario'] = UserProfile.objects.get(user = request.user)
    dict_context['validador']=0
    dict_context['categoria_form'] = CategoriaForm()
    return render(request, 'libreria/agregar_categoria.html',dict_context)

@login_required
def agregar_libro(request):
    context_dict = {}
    if request.method == "POST":
        libro_form = ProductoForm(request.POST)
        if libro_form.is_valid():
            i = 0
            print request.POST.get('numero_productos')
            j = Producto.objects.all().order_by('-id')[0]
            j = j.id+1
            while(i< int(request.POST.get('numero_productos'))):
                producto = libro_form.save(commit = False)
                fecha = date.today()
                producto.agregado_el_anio = fecha.year
                producto.agregado_el_mes = fecha.month
                producto.agregado_el_dia = fecha.day
                producto.vendido = 0
                producto.id = j
                producto.save()
                i = i+1
                j = j+1
            context_dict['articulo_form'] = ArticuloForm()
            context_dict['libro_form'] = ProductoForm()
            context_dict['validador'] = 1
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
            return render(request,'libreria/agregar_libro.html', context_dict)
        else:
            context_dict['validador'] = 0
            context_dict['articulo_form'] = ArticuloForm()
            context_dict['libro_form'] = libro_form
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
            return render(request,'libreria/agregar_libro.html', context_dict)
    context_dict['usuario'] = UserProfile.objects.get(user = request.user)
    context_dict['articulo_form'] = ArticuloForm()
    context_dict['libro_form'] = ProductoForm()
    return render(request,'libreria/agregar_libro.html', context_dict)

@login_required
def agregar_articulo(request):
    context_dict = {}
    if request.method == 'POST':
        articulo_form = ArticuloForm(request.POST)
        if articulo_form.is_valid():
            articulo = Articulo()
            articulo.nombre = request.POST.get('nombre')
            articulo.sucursal = 0
            if 'imagen' in request.FILES:
                articulo.imagen = request.FILES['imagen']
            articulo.save()
            context_dict['articulo_form'] = ArticuloForm()
            context_dict['libro_form'] = ProductoForm()
            context_dict['validador'] = 1
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
            return render(request,'libreria/agregar_libro.html', context_dict)
        else:
            context_dict['validador'] = 0
            context_dict['articulo_form'] = articulo_form
            context_dict['libro_form'] = ProductoForm()
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
            return render(request,'libreria/agregar_libro.html', context_dict)
    context_dict['usuario'] = UserProfile.objects.get(user = request.user)
    context_dict['articulo_form'] = ArticuloForm()
    context_dict['libro_form'] = ProductoForm()
    return render(request,'libreria/agregar_libro.html', context_dict)

@login_required
def muestra_categoria(request,categoria_nombre_slug):
    context_dict = {}
    try:
        categoria = Categoria.objects.get(slug = categoria_nombre_slug)
        context_dict['categoria'] = categoria
        libros = Producto.objects.all().filter(categoria = categoria).values('nombre_libro').distinct()
        dict = []
        for libro in libros:
            lib = Articulo.objects.get(id =int(libro['nombre_libro']))
            pro = Producto.objects.all().filter(nombre_libro_id = int(libro['nombre_libro']))
            dict_dict = {
                'nombre' : lib,
                'vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(libro['nombre_libro']), vendido = 1).count()),
                'no_vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(libro['nombre_libro']), vendido = 0).count()),
                'precio': str(pro[0].precio),
                'costo': str(pro[0].costo),
                'codigo_barras': str(pro[0].codigo_barras)
            }
            dict.append(dict_dict)
        context_dict['usuario'] = UserProfile.objects.get(user = request.user)
        context_dict['libros'] = dict
    except Categoria.DoesNotExist:
        context_dict['usuario'] = UserProfile.objects.get(user = request.user)
        context_dict['validador'] = 0

    return render(request,'libreria/busqueda_categoria.html',context_dict)

@login_required
def caja_ventas(request):
    context_dict = {}
    context_dict['validador'] = 0
    context_dict['usuario'] = UserProfile.objects.get(user = request.user)
    return render(request,'libreria/caja_registradora.html', context_dict)

@login_required
def muestra_libro(request, libro_slug):
    context_dict = {}
    try:
        libro = Articulo.objects.get(slug = libro_slug,sucursal=0)
        context_dict['titulo'] = libro
        dict = []
        pro = Producto.objects.all().filter(nombre_libro = libro)
        if (len(pro) != 0):
            dict_dict = {
                        'nombre': libro.nombre,
                        'vendidos':str(Producto.objects.all().filter(nombre_libro_id = int(libro.id), vendido = 1).count()),
                        'no_vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(libro.id),vendido = 0).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
                        'codigo_barras': str(pro[0].codigo_barras)
            }
            dict.append(dict_dict)
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
            context_dict['libros'] = dict
    except libro.DoesNotExist:
        context_dict['usuario'] = UserProfile.objects.get(user = request.user)

    return render(request,'libreria/busqueda_libro.html',context_dict)

@login_required
def ventas_caja(request):
    if request.method == 'GET':
        id_producto = request.GET['codigo']
        validador = request.GET['cancelado']
        salvar = Producto.objects.get(id = id_producto)
        nombre = Articulo.objects.get(id = salvar.nombre_libro_id)
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
def cambiar_precio_libro(request):
    context_dict = {}
    if request.method == 'POST':
        precio_form = Cambiar_precio_form(request.POST)
        if precio_form.is_valid():
            busqueda = Producto.objects.all().filter(nombre_libro_id = request.POST.get('producto')).exclude(vendido = 1)
            for producto in busqueda:
                producto.precio = request.POST.get('precio')
                producto.save()
            context_dict['validador'] = 2
            context_dict['precio_form'] = Cambiar_precio_form()
            context_dict['libreria_val'] = 1
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
            return render(request,'libreria/cambiar_precio_libro.html', context_dict)
        else:
            context_dict['usuario'] = UserProfile.objects.get(user = request.user)
            context_dict['libreria_val'] = 1
            context_dict['validador'] = 0
            context_dict['precio_form'] = precio_form
            return render(request, 'libreria/cambiar_precio_libro.html', context_dict)
    context_dict['usuario'] = UserProfile.objects.get(user = request.user)
    context_dict['libreria_val'] = 1
    context_dict['validador'] = 0
    context_dict['precio_form'] = Cambiar_precio_form()
    return render(request, 'libreria/cambiar_precio_libro.html', context_dict)

@login_required
def borrar_libro(request):
    context_dict = {}
    if request.method == 'POST':
        borrar_form = borrar_libro_form(request.POST)
        if borrar_form.is_valid():
            borrar = Producto.objects.all().filter(nombre_libro_id = int(request.POST.get('producto')), vendido = 0)
            for b in borrar:
                b.delete()
        context_dict['usuario'] = UserProfile.objects.get(user = request.user)
        context_dict['validador'] = 3
        context_dict['borrar_form'] = borrar_libro_form()
    else:
        context_dict['usuario'] = UserProfile.objects.get(user = request.user)
        context_dict['validador'] = 0
        context_dict['borrar_form'] = borrar_libro_form()
    return render(request,'libreria/borrar_libro.html', context_dict)



