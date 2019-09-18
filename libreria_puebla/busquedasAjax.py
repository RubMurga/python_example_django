__author__ = 'RubenMurga'

from django.http import HttpResponse
from libreria.models import Articulo, Categoria, Producto
from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required

@login_required
def busqueda_libro(request):
    empieza_con = ''
    regreso = []
    if request.method == 'GET':
        empieza_con = request.GET['sugerencia']
        if empieza_con == '':
            return HttpResponse('')
        else:
            regreso = Articulo.objects.filter(nombre__istartswith = empieza_con,sucursal=1)
            if regreso:
                return render(request,'libreria/sugerencias.html',{'sugerencias_libros':regreso})
            else:
                return HttpResponse('')

@login_required
def busqueda_libro_cb(request):
    empieza_con = ''
    regreso = []
    if request.method == 'GET':
        empieza_con = request.GET['sugerencia']
        if empieza_con == '':
            return HttpResponse('')
        else:
            busqueda = Producto.objects.all().filter(codigo_barras = empieza_con)
            regreso = Articulo.objects.filter(id = int(busqueda[0].nombre_libro_id),sucursal=1)
            if regreso:
                return render(request,'libreria/sugerencias.html',{'sugerencias_libros':regreso})
            elif (len(busqueda==0)):
                return HttpResponse('')

@login_required
def busqueda_categoria(request):
    empieza_con = ''
    regreso = []
    if request.method == 'GET':
        empieza_con = request.GET['sugerencia']
        if empieza_con == '':
            return HttpResponse('')
        else:
            regreso = Categoria.objects.filter(nombre_categoria__istartswith = empieza_con)
            if regreso:
                return render(request, 'libreria/sugerencias.html', {'sugerencias_categorias':regreso})
            else:
               return HttpResponse('')

@login_required
def busquedaCaja(request):
    if request.method == 'GET':
        codigo_barras = request.GET['codigo']
        busqueda = Producto.objects.all().filter(codigo_barras = codigo_barras).exclude(vendido=1).exclude(en_caja=1)[:1]
        busqueda2 = Articulo.objects.get(id = busqueda[0].nombre_libro_id,sucursal=1)
        salvar = Producto.objects.get(id = busqueda[0].id)
        salvar.en_caja = 1
        salvar.save()
        return HttpResponse(json.dumps({'nombre':busqueda2.nombre, 'precio':str(salvar.precio), 'id':str(salvar.id)}),content_type = 'aplication/json')

@login_required
def busqueda_libreria(request):
    if request.method == 'GET':
        nombre_articulo = request.GET['nombre_art']
        busqueda = Articulo.objects.get(nombre = nombre_articulo,sucursal=1)
        return HttpResponse(json.dumps({'nombre':busqueda.nombre}),content_type = 'aplication/json')

@login_required
def busqueda_categoria_angular(request):
    if request.method == 'GET':
        nombre_categoria = request.GET['nombre_cat']
        busqueda = Categoria.objects.get(nombre_categoria =nombre_categoria )
        return HttpResponse(json.dumps({'nombre':busqueda.nombre_categoria}),content_type = 'aplication/json')