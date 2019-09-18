# -*- coding: utf-8 -*-

__author__ = 'RubenMurga'

from django import forms
from cafeteria.models import productos, Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('nombre',)

    def __init__(self,*args,**kwargs):
        super(ArticuloForm,self).__init__(*args,**kwargs)

        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['placeholder'] = 'Introduce un nombre para el producto'
        self.fields['nombre'].label = 'Nombre producto a agregar'
        self.fields['nombre'].error_messages['required'] = "Debes introducir un nombre para el producto"
        self.fields['nombre'].initial = ""
        self.fields['nombre'].widget.attrs['ng-model'] = 'cafeteria_input'
        self.fields['nombre'].widget.attrs['ng-change'] = 'buscar_producto()'




class productosForm(forms.ModelForm):
    porcentaje = forms.IntegerField()
    nombre_producto = forms.ModelChoiceField(queryset = Articulo.objects.filter(sucursal=1), widget = forms.Select(attrs={'class':'form-control'}), label = 'Nombre del producto' )
    numero_productos = forms.IntegerField()
    class Meta:
        model = productos
        fields = ('nombre_producto','costo','porcentaje','precio','numero_productos', 'codigo_barras')
        exclude = ('vendido', 'vendido_por', 'agregado_el_anio','agregado_el_mes','agregado_el_dia','vendido_el_anio', 'vendido_el_mes','vendido_el_dia','en_caja')
    def __init__(self,*args, **kwargs):
        super(productosForm,self).__init__(*args, **kwargs)
        self.fields['codigo_barras'].widget = forms.TextInput()
        self.fields['codigo_barras'].label = 'Codigo de barras'
        self.fields['codigo_barras'].widget.attrs['placeholder'] = '00000000000000'
        self.fields['codigo_barras'].error_messages['invalid'] = 'Debes introducir numeros'
        self.fields['codigo_barras'].initial = ""
        self.fields['codigo_barras'].widget.attrs['class'] = 'form-control'

        self.fields['numero_productos'].widget.attrs['class'] = 'form-control'
        self.fields['numero_productos'].widget.attrs['placeholder'] = 'Introduce el número de productos'
        self.fields['numero_productos'].label = 'Número de productos a agregar'
        self.fields['numero_productos'].error_messages['required'] = "Debes introducir un numero de productos"
        self.fields['numero_productos'].initial = ""

        self.fields['costo'].widget = forms.TextInput()
        self.fields['costo'].initial = ""
        self.fields['costo'].widget.attrs['class'] = 'form-control'
        self.fields['costo'].widget.attrs['placeholder'] = '$ 0.0'
        self.fields['costo'].error_messages['required'] = "Debes llenar este campo"
        self.fields['costo'].error_messages['invalid'] = "Debe ser un numero"
        self.fields['costo'].label = 'Precio de compra'
        self.fields['costo'].widget.attrs['ng-model'] = 'costo_input_cafe'
        self.fields['costo'].widget.attrs['autocomplete'] = 'off'
        self.fields['costo'].widget.attrs['ng-change'] = 'calcular_precio_cafeteria()'


        self.fields['porcentaje'].widget = forms.TextInput()
        self.fields['porcentaje'].initial = ""
        self.fields['porcentaje'].widget.attrs['class'] = 'form-control'
        self.fields['porcentaje'].widget.attrs['placeholder'] = '0%'
        self.fields['porcentaje'].error_messages['required'] = "Debes llenar este campo"
        self.fields['porcentaje'].error_messages['invalid'] = "Debe ser un numero"
        self.fields['porcentaje'].label = 'Porcentaje de ganancia por producto'
        self.fields['porcentaje'].widget.attrs['ng-model'] = 'porcentaje_input_cafeteria'
        self.fields['porcentaje'].widget.attrs['ng-change'] = 'calcular_precio_cafeteria()'
        self.fields['porcentaje'].widget.attrs['autocomplete'] = 'off'


        self.fields['nombre_producto'].error_messages['invalid'] = "Debes cumplir con el formado requerido"
        self.fields['nombre_producto'].error_messages['required'] = "Debes escoger un articulo"

        self.fields['precio'].widget = forms.TextInput()
        self.fields['precio'].initial = ""
        self.fields['precio'].label = 'Precio de venta del producto'
        self.fields['precio'].widget.attrs['placeholder'] = '$ 0.0'
        self.fields['precio'].error_messages['invalid'] = "Debes introducir numeros "
        self.fields['precio'].widget.attrs['class'] = 'form-control'
        self.fields['precio'].widget.attrs['value'] = '[[precio_pro_cafeteria]]'
        self.fields['precio'].widget.attrs['autocomplete'] = 'off'

class Cambiar_precio_form(forms.Form):
    producto = forms.ModelChoiceField(queryset = Articulo.objects.filter(sucursal=1),widget = forms.Select(attrs={'class':'form-control'}), label = 'Nombre del producto' )
    precio = forms.DecimalField()

    def __init__(self,*args,**kwargs):
        super(Cambiar_precio_form,self).__init__(*args, **kwargs)
        self.fields['producto'].error_messages['required'] = "Debes escoger un articulo"
        self.fields['producto'].error_messages['invalid'] = "Debes cumplir con el formato"
        self.fields['precio'].widget = forms.TextInput()
        self.fields['precio'].initial = ""
        self.fields['precio'].widget.attrs['class'] = 'form-control'
        self.fields['precio'].widget.attrs['placeholder'] = '$ 0.0'
        self.fields['precio'].error_messages['required'] = "Debes llenar este campo"
        self.fields['precio'].error_messages['invalid'] = "Debe ser un numero"
        self.fields['precio'].required = True

class borrar_producto_form(forms.Form):
    producto = forms.ModelChoiceField(queryset = Articulo.objects.filter(sucursal=1),widget = forms.Select(attrs={'class':'form-control'}), label = 'Nombre del producto' )

    def __init__(self,*args,**kwargs):
        super(borrar_producto_form,self).__init__(*args, **kwargs)
        self.fields['producto'].error_messages['required'] = "Debes escoger un articulo"
        self.fields['producto'].error_messages['invalid'] = "Debes cumplir con el formato"





