# -*- coding: utf-8 -*-

__author__ = 'RubenMurga'
from django import forms
from cafeteria.models import Articulo as Articulo_cafeteria ,productos
from libreria.models import Articulo as Articulo_libreria, Producto
from comercializadora.models import Articulo_comercializadora
from django.contrib.auth.models import User
from registro.models import UserProfile
class form_user(forms.ModelForm):
    usuarios = User.objects.all()
    dict = []
    for usuario in usuarios:
        dict_dict = (
            (usuario.id , usuario)
        )
        busqueda = UserProfile.objects.get(user = usuario)
        if busqueda.belongs_to == 'Libreria' or busqueda.belongs_to == 'Administrador':
            dict.append(dict_dict)
    lista_usuarios = forms.ChoiceField(choices = dict , widget = forms.Select(attrs = {'class': 'form-control', 'ng-model':'vendedor_libreria', 'ng-change':'busca_vendedor_func()'}), label = 'Vendidos por' )
    class Meta:
        model = User
        fields = ('lista_usuarios',)

class form_libro(forms.ModelForm):
    nombre_libro = forms.ModelChoiceField(queryset = Articulo_libreria.objects.all().filter(sucursal=0) ,widget = forms.Select(attrs={'class':'form-control', 'ng-change':'busca_libro_func()', 'ng-model':'libro_input'}), label = 'Nombre del libro' )
    class Meta:
        model = Articulo_libreria
        fields = ('nombre_libro',)

class form_comercializadora(forms.ModelForm):
    nombre_libro = forms.ModelChoiceField(queryset = Articulo_comercializadora.objects.all() ,widget = forms.Select(attrs={'class':'form-control', 'ng-change':'busca_libro_func()', 'ng-model':'libro_input'}), label = 'Nombre del articulo' )
    class Meta:
        model = Articulo_libreria
        fields = ('nombre_libro',)

class form_cafeteria(forms.ModelForm):
    nombre_producto = forms.ModelChoiceField(queryset = Articulo_cafeteria.objects.all().filter(sucursal=0) ,widget = forms.Select(attrs={'class':'form-control', 'ng-change':'busca_producto_func()', 'ng-model':'producto_input'}), label = 'Nombre del producto' )
    class Meta:
        model = Articulo_libreria
        fields = ('nombre_producto',)

class form_user_cafeteria(forms.ModelForm):
    usuarios = User.objects.all()
    dict = []
    dict_dict = (0, '--------')
    dict.append(dict_dict)
    for usuario in usuarios:
        dict_dict = (
            (usuario.id , usuario)
        )
        busqueda = UserProfile.objects.get(user = usuario)
        if busqueda.belongs_to == 'Cafeteria' or busqueda.belongs_to == 'Administrador':
            dict.append(dict_dict)
    lista_usuarios = forms.ChoiceField(choices = dict , widget = forms.Select(attrs = {'class': 'form-control', 'ng-model':'vendedor_cafeteria', 'ng-change':'busca_vendedor_func()'}), label = 'Vendidos por' )
    class Meta:
        model = User
        fields = ('lista_usuarios',)

class month_form(forms.Form):
    months = [
        (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'),
        (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'),
        (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'),
        (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')
        ]
    months_choises = forms.ChoiceField(choices = months, widget = forms.Select(attrs = {'class': 'form-control', 'ng-model':'mes_busqueda'}), label = 'Mes')

    class Meta:
        fields = ('months_choises',)

class year_form(forms.Form):
    years = [
        (2019, '2019'), (2018, '2018'), (2017, '2017'),
        (2016, '2016'), (2017, '2015'), (2016, '2014')
        ]
    years_choises = forms.ChoiceField(choices = years, widget = forms.Select(attrs = {'class': 'form-control', 'ng-model':'anio_busqueda'}), label = 'Año')

    class Meta:
        fields = ('years_choises',)


