__author__ = 'RubenMurga'

from django.http import HttpResponse
from cafeteria.models import Articulo, productos
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def busquedaCaja(request):
    if request.method == 'GET':
        codigo_barras = str(request.GET['codigo'])
        busqueda = productos.objects.all().filter(codigo_barras = codigo_barras).exclude(vendido=1).exclude(en_caja=1)[:1]
        salvar = productos.objects.get(id = busqueda[0].id)
        salvar.en_caja = 1
        salvar.save()
        busqueda2 = Articulo.objects.get(id = salvar.nombre_producto_id,sucursal=0)
        return HttpResponse(json.dumps({'nombre':busqueda2.nombre, 'precio':str(salvar.precio), 'id': str(salvar.id)}),content_type = 'aplication/json')

@login_required
def busqueda_articulo(request):
    if request.method == 'GET':
        nombre_articulo = request.GET['nombre_art']
        try:
            busqueda = Articulo.objects.get(nombre = nombre_articulo,sucursal=0)
            return HttpResponse(json.dumps({'nombre':busqueda.nombre}),content_type = 'aplication/json')
        except Exception as error: 
            return HttpResponse(json.dumps({'no_encontrado': True}),content_type = 'aplication/json')

@login_required
def busqueda_producto(request):
    empieza_con = ''
    regreso = []
    if request.method == 'GET':
        empieza_con = request.GET['sugerencia']
        if empieza_con == '':
            return HttpResponse('')
        else:
            regreso = Articulo.objects.filter(nombre__istartswith = empieza_con,sucursal=0)
            if regreso:
                return render(request,'cafeteria/sugerencias.html',{'sugerencias_libros':regreso})
            else:
                return HttpResponse('')
@login_required
def busqueda_producto_cb(request):
    empieza_con = ''
    regreso = []
    if request.method == 'GET':
        empieza_con = request.GET['sugerencia']
        if empieza_con == '':
            return HttpResponse('')
        else:
            busqueda = productos.objects.all().filter(codigo_barras = empieza_con)
            regreso = Articulo.objects.filter(id = int(busqueda[0].nombre_producto_id),sucursal=0)
            if regreso and busqueda:
                return render(request,'cafeteria/sugerencias.html',{'sugerencias_libros':regreso})
            else:
                return HttpResponse('')
