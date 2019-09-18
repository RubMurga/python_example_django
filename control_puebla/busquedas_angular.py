__author__ = 'RubenMurga'
import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from cafeteria.models import productos, Articulo as Articulo_cafeteria
from libreria.models import Producto,Articulo as Articulo_libreria
#from comercializadora.models import Producto_comercializadora, Articulo_comercializadora
from registro.models import UserProfile
from datetime import date
from control_puebla.ventas_semana import ventas_semana_ven,ventas_semana_libreria_inicial, ventas_semana_cafeteria_inicial #,ventas_semana_comercializadora_inicial
from django.contrib.auth.decorators import login_required

@login_required
def acabando_productos(request):
    if request.method == 'GET':
        dict = []
        productos_cafeteria = Articulo_cafeteria.objects.all().filter(sucursal=1)
        libros_libreria = Articulo_libreria.objects.all().filter(sucursal=1)
        #productos_comercializadora = Articulo_comercializadora.objects.all()
        for producto in productos_cafeteria:
            restantes = productos.objects.all().filter(nombre_producto = producto,vendido = 0).count()
            dict_dict = {
                'nombre': producto.nombre,
                'restantes':str(restantes),
                'pertenece': 'cafeteria',
            }
            dict.append(dict_dict)

        for libro in libros_libreria:
            restantes = Producto.objects.all().filter(nombre_libro = libro,vendido = 0).count()
            dict_dict = {
                'nombre': libro.nombre,
                'restantes':str(restantes),
                'pertenece': 'libreria',
            }
            dict.append(dict_dict)
        """
        for producto_comer in productos_comercializadora:
            restantes = Producto_comercializadora.objects.all().filter(nombre_articulo = producto_comer, vendido=0).count()
            dict_dict = {
                'nombre': producto_comer.nombre,
                'restantes':str(restantes),
                'pertenece': 'Comercializadora',
            }
            dict.append(dict_dict)
        """
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

#metodo para el inicio del control
@login_required
def busqueda_vendedores_dia(request):
    if request.method == 'GET':
        vendedores = User.objects.all()
        dict = []
        hoy = date.today()
        for vendedor in vendedores:
            validador = UserProfile.objects.get(user = vendedor)
            ventas_semana_libreria, ventas_semana_cafeteria = ventas_semana_ven(vendedor)
            dict_dict = {
                'nombre': vendedor.username,
                'ventas_cafeteria_dia': str(productos.objects.all().filter(vendido_por = vendedor,vendido_el_dia = hoy.day, vendido_el_mes = hoy.month,vendido_el_anio = hoy.year).count()),
                'ventas_libreria_dia': str(Producto.objects.all().filter(vendido_por = vendedor,vendido_el_dia = hoy.day, vendido_el_mes = hoy.month,vendido_el_anio = hoy.year).count()),
                #'ventas_comercializadora_dia': str(Producto_comercializadora.objects.all().filter(vendido_por = vendedor,vendido_el_dia = hoy.day, vendido_el_mes = hoy.month,vendido_el_anio = hoy.year).count()),
                'ventas_cafeteria_semana': str(ventas_semana_cafeteria),
                'ventas_libreria_semana': str(ventas_semana_libreria),
                #'ventas_comercializadora_semana': str(ventas_semana_comercializadora),
                #'ventas_comercializadora_mes': str(Producto_comercializadora.objects.all().filter(vendido_por = vendedor,vendido_el_mes = hoy.month,vendido_el_anio = hoy.year).count()),
                'ventas_cafeteria_mes': str(productos.objects.all().filter(vendido_por = vendedor,vendido_el_mes = hoy.month,vendido_el_anio = hoy.year).count()),
                'ventas_libreria_mes': str(Producto.objects.all().filter(vendido_por = vendedor,vendido_el_mes = hoy.month,vendido_el_anio = hoy.year).count()),
                'belongs_to' : validador.belongs_to,
            }
            dict.append(dict_dict)
        return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

#dia libreria
@login_required
def busqueda_inicial_libros_dia(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        productos_registrados = Articulo_libreria.objects.all().filter(sucursal=1)
        for producto in productos_registrados:
            pro = Producto.objects.all().filter(nombre_libro = producto)
            if(len(pro) != 0):
                dict_dict = {
                    'nombre': producto.nombre,
                    'vendidos':str(Producto.objects.all().filter(nombre_libro_id = int(producto.id), vendido = 1, vendido_el_dia = hoy.day, vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()),
                    'precio': str(pro[0].precio),
                    'costo': str(pro[0].costo),
                }
                dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_vendedor_dia(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        libros_vendidos = Producto.objects.all().filter(vendido = 1, vendido_por = int(request.GET['vendedor']), vendido_el_dia = hoy.day, vendido_el_mes = hoy.month, vendido_el_anio = hoy.year)
        for libro in libros_vendidos:
            vendido_por = User.objects.get(id = libro.vendido_por_id)
            dict_dict = {
                'nombre': str(Articulo_libreria.objects.all().filter(id = libro.nombre_libro_id,sucursal=1)),
                'vendido_por':vendido_por.first_name,
                'costo': str(libro.costo),
                'precio': str(libro.precio)
            }
            valida = UserProfile.objects.get(id = vendido_por.id)
            if valida.belongs_to == 'Libreria':
                dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_libro_dia(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        producto = Articulo_libreria.objects.get(id = int(request.GET['libro']),sucursal=1)
        pro = Producto.objects.all().filter(nombre_libro = producto)
        if (len(pro) != 0):
            dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(Producto.objects.all().filter(nombre_libro_id = int(producto.id), vendido = 1, vendido_el_mes = hoy.month, vendido_el_dia = hoy.day, vendido_el_anio = hoy.year).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
            }
            dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

# Semana libreria
@login_required
def busqueda_libro_semana_inicial(request):
    if request.method == 'GET':
        dict = ventas_semana_libreria_inicial(0,0)
        return HttpResponse(json.dumps(dict), content_type = 'aplication/json')
@login_required
def busqueda_libro_semana_vendedor(request):
    if request.method == 'GET':
        dict = ventas_semana_libreria_inicial(int(request.GET['vendedor']),0)
        return HttpResponse(json.dumps(dict), content_type = 'aplication/json')
@login_required
def busqueda_libro_semana_libro(request):
    if request.method == 'GET':
        dict = ventas_semana_libreria_inicial(0,int(request.GET['libro']))
        return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

#libreria mes
@login_required
def busqueda_inicial_libros_mes(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        productos_registrados = Articulo_libreria.objects.all().filter(sucursal=1)
        for producto in productos_registrados:
            pro = Producto.objects.all().filter(nombre_libro = producto)
            if(len(pro) != 0):
                dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(Producto.objects.all().filter(nombre_libro_id = int(producto.id), vendido = 1,  vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
                }
                dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_vendedor_mes(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        libros_vendidos = Producto.objects.all().filter(vendido = 1, vendido_el_mes = hoy.month,vendido_el_anio = hoy.year, vendido_por = int(request.GET['vendedor']))
        for libro in libros_vendidos:
            vendido_por = User.objects.get(id = libro.vendido_por_id)
            dict_dict = {
                'nombre': str(Articulo_libreria.objects.all().filter(id = libro.nombre_libro_id,sucursal=1)),
                'vendido_por': vendido_por.first_name,
                'costo': str(libro.costo),
                'precio': str(libro.precio),
                'vendido_el_dia': str(libro.vendido_el_dia),
            }
            valida = UserProfile.objects.get(id = vendido_por.id)
            if valida.belongs_to == 'Libreria':
                dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_libro_mes(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        producto = Articulo_libreria.objects.get(id = int(request.GET['libro']),sucursal=1)
        pro = Producto.objects.all().filter(nombre_libro = producto)
        if (len(pro) != 0):
            dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(Producto.objects.all().filter(nombre_libro_id = int(producto.id), vendido = 1, vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
            }
            dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')



#busqueda todos registrados
@login_required
def busqueda_todos_libros(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        libros_registrados = Articulo_libreria.objects.all().filter(sucursal=1)
        for libro in libros_registrados:
            pro = Producto.objects.all().filter(nombre_libro = libro)
            if(len(pro) != 0):
                dict_dict = {
                    'nombre': libro.nombre,
                    'vendidos':str(Producto.objects.all().filter(nombre_libro_id = int(libro.id), vendido = 1).count()),
                    'no_vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(libro.id),vendido = 0).count()),
                    'precio': str(pro[0].precio),
                    'costo': str(pro[0].costo),
                }
                dict.append(dict_dict)

    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_todos_libro_especifico(request):
    if request.method == 'GET':
        dict = []
        producto = Articulo_libreria.objects.get(id = int(request.GET['libro']),sucursal=1)
        pro = Producto.objects.all().filter(nombre_libro = producto)
        if (len(pro) != 0):
            dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(Producto.objects.all().filter(nombre_libro_id = int(producto.id), vendido = 1).count()),
                        'no_vendidos': str(Producto.objects.all().filter(nombre_libro_id = int(producto.id),vendido = 0).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
            }
            dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')






# cafeteria dia
@login_required
def busqueda_inicial_cafeteria_dia(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        productos_registrados = Articulo_cafeteria.objects.all().filter(sucursal=1)
        for producto in productos_registrados:
            pro = productos.objects.all().filter(nombre_producto = producto)
            if(len(pro) != 0):
                dict_dict = {
                    'nombre': producto.nombre,
                    'vendidos':str(productos.objects.all().filter(nombre_producto_id = int(producto.id), vendido = 1,vendido_el_dia = hoy.day, vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()),
                    'precio': str(pro[0].precio),
                    'costo': str(pro[0].costo),
                }
                dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_vendedor_dia_cafeteria(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        productos_vendidos = productos.objects.all().filter(vendido = 1, vendido_por = int(request.GET['vendedor']), vendido_el_dia = hoy.day, vendido_el_mes = hoy.month, vendido_el_anio = hoy.year)
        for producto in productos_vendidos:
            vendido_por = User.objects.get(id = producto.vendido_por_id)
            dict_dict = {
                'nombre': str(Articulo_cafeteria.objects.get(id = producto.nombre_producto_id,sucursal=1)),
                'vendido_por': vendido_por.first_name,
                'costo': str(producto.costo),
                'precio': str(producto.precio),
                'vendido_el_dia': str(producto.vendido_el_dia)

            }
            valida = UserProfile.objects.get(id = vendido_por.id)
            if valida.belongs_to == 'Cafeteria':
                dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_producto_dia_cafeteria(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        producto = Articulo_cafeteria.objects.get(id = int(request.GET['producto']),sucursal=1)
        pro = productos.objects.all().filter(nombre_producto = producto)
        if (len(pro) != 0):
            dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(productos.objects.all().filter(nombre_producto_id = int(producto.id),vendido_el_dia = hoy.day, vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
            }
            dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')


#semana cafeteria
@login_required
def busqueda_producto_semana_inicial(request):
    if request.method == 'GET':
        dict = ventas_semana_cafeteria_inicial(0,0)
        return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_producto_semana_vendedor(request):
    if request.method == 'GET':
        dict = ventas_semana_cafeteria_inicial(int(request.GET['vendedor']),0)
        return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_producto_semana(request):
    if request.method == 'GET':
        dict = ventas_semana_cafeteria_inicial(0,int(request.GET['producto']))
        return HttpResponse(json.dumps(dict), content_type = 'aplication/json')


#cafeteria mes
@login_required
def busqueda_inicial_cafeteria_mes(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        productos_registrados = Articulo_cafeteria.objects.all().filter(sucursal=1)
        for producto in productos_registrados:
            pro = productos.objects.all().filter(nombre_producto = producto)
            if(len(pro) != 0):
                dict_dict = {
                    'nombre': producto.nombre,
                    'vendidos':str(productos.objects.all().filter(nombre_producto_id = int(producto.id), vendido = 1, vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()),
                    'precio': str(pro[0].precio),
                    'costo': str(pro[0].costo),
                }
                dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_vendedor_mes_cafeteria(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        productos_vendidos = productos.objects.all().filter(vendido = 1,vendido_el_mes = hoy.month, vendido_el_anio = hoy.year, vendido_por = int(request.GET['vendedor']))
        for producto in productos_vendidos:
            vendido_por = User.objects.get(id = producto.vendido_por_id)
            dict_dict = {
                'nombre': str(Articulo_cafeteria.objects.get(id = producto.nombre_producto_id,sucursal=1)),
                'vendido_por': vendido_por.first_name,
                'costo': str(producto.costo),
                'precio': str(producto.precio),
                'vendido_el_dia': str(producto.vendido_el_dia)
            }
            valida = UserProfile.objects.get(id = vendido_por.id)
            if valida.belongs_to == 'Cafeteria':
                dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_producto_mes_cafeteria(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        producto = Articulo_cafeteria.objects.get(id = int(request.GET['producto']),sucursal=1)
        pro = productos.objects.all().filter(nombre_producto = producto)
        if (len(pro) != 0):
            dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(productos.objects.all().filter(nombre_producto_id = int(producto.id), vendido = 1, vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
            }
            dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')


#todos los productos cafeteria
@login_required
def busqueda_todos_productos(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        productos_registrados = Articulo_cafeteria.objects.all().filter(sucursal=1)
        for producto in productos_registrados:
            pro = productos.objects.all().filter(nombre_producto = producto)
            if(len(pro) != 0):
                dict_dict = {
                    'nombre': producto.nombre,
                    'vendidos':str(productos.objects.all().filter(nombre_producto_id = int(producto.id), vendido = 1).count()),
                    'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(producto.id),vendido = 0).count()),
                    'precio': str(pro[0].precio),
                    'costo': str(pro[0].costo),
                }
                dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_productos_especifico(request):
    if request.method == 'GET':
        dict = []
        producto = Articulo_cafeteria.objects.get(id = int(request.GET['producto']),sucursal=1)
        pro = productos.objects.all().filter(nombre_producto = producto)
        if (len(pro) != 0):
            dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(productos.objects.all().filter(nombre_producto_id = int(producto.id), vendido = 1).count()),
                        'no_vendidos': str(productos.objects.all().filter(nombre_producto_id = int(producto.id),vendido = 0).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
            }
            dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')


"""

#comercializadora
@login_required
def busqueda_inicial_comercializadora_dia(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        productos_registrados = Articulo_comercializadora.objects.all()
        for producto in productos_registrados:
            pro = Producto_comercializadora.objects.all().filter(nombre_articulo = producto)
            if(len(pro) != 0):
                dict_dict = {
                    'nombre': producto.nombre,
                    'vendidos':str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(producto.id), vendido = 1, vendido_el_dia = hoy.day, vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()),
                    'precio': str(pro[0].precio),
                    'costo': str(pro[0].costo),
                }
                dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_vendedor_comercializadora_dia(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        libros_vendidos = Producto_comercializadora.objects.all().filter(vendido = 1, vendido_por = int(request.GET['vendedor']), vendido_el_dia = hoy.day, vendido_el_mes = hoy.month, vendido_el_anio = hoy.year)
        for libro in libros_vendidos:
            vendido_por = User.objects.get(id = libro.vendido_por_id)
            dict_dict = {
                'nombre': str(Articulo_comercializadora.objects.get(id = libro.nombre_articulo_id)),
                'vendido_por': vendido_por.first_name,
                'costo': str(libro.costo),
                'precio': str(libro.precio)
            }
            valida = UserProfile.objects.get(id = vendido_por.id)
            dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_comercializadora_producto_dia(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        producto = Articulo_comercializadora.objects.get(id = int(request.GET['libro']))
        pro = Producto_comercializadora.objects.all().filter(nombre_articulo = producto)
        if (len(pro) != 0):
            dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(producto.id), vendido = 1, vendido_el_mes = hoy.month, vendido_el_dia = hoy.day, vendido_el_anio = hoy.year).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
            }
            dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

# Semana comercializadora
@login_required
def busqueda_comercializadora_semana_inicial(request):
    if request.method == 'GET':
        dict = ventas_semana_comercializadora_inicial(0,0)
        return HttpResponse(json.dumps(dict), content_type = 'aplication/json')
@login_required
def busqueda_comercializadora_semana_vendedor(request):
    if request.method == 'GET':
        dict = ventas_semana_comercializadora_inicial(int(request.GET['vendedor']),0)
        return HttpResponse(json.dumps(dict), content_type = 'aplication/json')
@login_required
def busqueda_comercializadora_semana_producto(request):
    if request.method == 'GET':
        dict = ventas_semana_comercializadora_inicial(0,int(request.GET['libro']))
        return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

#comercializadora mes
@login_required
def busqueda_inicial_comercializadora_mes(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        productos_registrados = Articulo_comercializadora.objects.all()
        for producto in productos_registrados:
            pro = Producto_comercializadora.objects.all().filter(nombre_articulo = producto)
            if(len(pro) != 0):
                dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(producto.id), vendido = 1,  vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
                }
                dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_comercializadora_vendedor_mes(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        libros_vendidos = Producto_comercializadora.objects.all().filter(vendido = 1, vendido_el_mes = hoy.month,vendido_el_anio = hoy.year, vendido_por = int(request.GET['vendedor']))
        for libro in libros_vendidos:
            vendido_por = User.objects.get(id = libro.vendido_por_id)
            dict_dict = {
                'nombre': str(Articulo_comercializadora.objects.get(id = libro.nombre_articulo_id)),
                'vendido_por': vendido_por.first_name,
                'costo': str(libro.costo),
                'precio': str(libro.precio),
                'vendido_el_dia': str(libro.vendido_el_dia),
            }
            dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_comercializadora_producto_mes(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        producto = Articulo_comercializadora.objects.get(id = int(request.GET['libro']))
        pro = Producto_comercializadora.objects.all().filter(nombre_articulo = producto)
        if (len(pro) != 0):
            dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(producto.id), vendido = 1, vendido_el_mes = hoy.month, vendido_el_anio = hoy.year).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
            }
            dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')



#busqueda todos registrados
@login_required
def busqueda_comercializadora_productos(request):
    if request.method == 'GET':
        dict = []
        hoy = date.today()
        libros_registrados = Articulo_comercializadora.objects.all()
        for libro in libros_registrados:
            pro = Producto_comercializadora.objects.all().filter(nombre_articulo = libro)
            if(len(pro) != 0):
                dict_dict = {
                    'nombre': libro.nombre,
                    'vendidos':str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(libro.id), vendido = 1).count()),
                    'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(libro.id),vendido = 0).count()),
                    'precio': str(pro[0].precio),
                    'costo': str(pro[0].costo),
                }
                dict.append(dict_dict)

    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

@login_required
def busqueda_todos_comercializadora_especifico(request):
    if request.method == 'GET':
        dict = []
        producto = Articulo_comercializadora.objects.get(id = int(request.GET['libro']))
        pro = Producto_comercializadora.objects.all().filter(nombre_articulo = producto)
        if (len(pro) != 0):
            dict_dict = {
                        'nombre': producto.nombre,
                        'vendidos':str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(producto.id), vendido = 1).count()),
                        'no_vendidos': str(Producto_comercializadora.objects.all().filter(nombre_articulo_id = int(producto.id),vendido = 0).count()),
                        'precio': str(pro[0].precio),
                        'costo': str(pro[0].costo),
            }
            dict.append(dict_dict)
    return HttpResponse(json.dumps(dict), content_type = 'aplication/json')

"""


