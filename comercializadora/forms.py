__author__ = 'RubenMurga'

__author__ = 'RubenMurga'

from django import forms
from comercializadora.models import Categoria_comercializadora as Categoria, Producto_comercializadora as Producto, Articulo_comercializadora as Articulo
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre_categoria',)

    def __init__(self,*args,**kwargs):
        super(CategoriaForm,self).__init__(*args, **kwargs)
        self.fields['nombre_categoria'].widget.attrs['class'] = 'form-control'
        self.fields['nombre_categoria'].widget.attrs['placeholder'] = 'Introduce un nombre para la nueva categoria'
        self.fields['nombre_categoria'].label = 'Nombre de la categoria'
        self.fields['nombre_categoria'].error_messages['required'] = "Debes introducir una categoria"
        self.fields['nombre_categoria'].initial = ""
        self.fields['nombre_categoria'].widget.attrs['ng-model'] = 'categoria_input'
        self.fields['nombre_categoria'].widget.attrs['ng-change'] = 'buscarCategoria()'


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('nombre',)

    def __init__(self,*args,**kwargs):
        super(ArticuloForm,self).__init__(*args,**kwargs)

        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['placeholder'] = 'Introduce un nombre para el producto'
        self.fields['nombre'].label = 'Nombre del producto a agregar'
        self.fields['nombre'].error_messages['required'] = "Debes introducir un nombre para el producto"
        self.fields['nombre'].initial = ""
        self.fields['nombre'].widget.attrs['ng-model'] = 'libreria_input'
        self.fields['nombre'].widget.attrs['ng-change'] = 'buscarProducto()'


        """
        self.fields['imagen'].widget = forms.ClearableFileInput(attrs={
            'label': 'foto de perfil',
            'class': 'filestyle',
            'data-buttonName':'btn-primary',
        })
        self.fields['imagen'].label = "imagen de perfil"
        """

class ProductoForm(forms.ModelForm):
    porcentaje = forms.IntegerField()
    categoria = forms.ModelChoiceField(queryset = Categoria.objects.all(),widget = forms.Select(attrs={'class':'form-control'}), label = 'Categoria del Producto')
    numero_productos = forms.IntegerField()
    class Meta:
        model = Producto
        fields = ('nombre_articulo','costo','porcentaje','precio','numero_productos','categoria','codigo_barras')
        exclude = ('vendido','vendido_por','agregado_el_anio','agregado_el_mes','agregado_el_dia','vendido_el_anio','vendido_el_mes','vendido_el_dia','en_caja')
    def __init__(self,*args,**kwargs):
        super(ProductoForm,self).__init__(*args,**kwargs)
        self.fields['nombre_articulo'].error_messages['required'] = "Debes escoger un articulo"
        self.fields['nombre_articulo'].error_messages['invalid'] = "Debes cumplir con el formato"

        self.fields['precio'].widget = forms.TextInput()
        self.fields['precio'].initial = ""
        self.fields['precio'].widget.attrs['class'] = 'form-control'
        self.fields['precio'].widget.attrs['placeholder'] = '$ 0.0'
        self.fields['precio'].error_messages['required'] = "Debes llenar este campo"
        self.fields['precio'].error_messages['invalid'] = "Debe ser un numero"
        self.fields['precio'].label = 'Precio de venta'
        self.fields['precio'].widget.attrs['value'] = '[[precio_input]]'
        self.fields['precio'].widget.attrs['autocomplete'] = 'off'

        self.fields['costo'].widget = forms.TextInput()
        self.fields['costo'].initial = ""
        self.fields['costo'].widget.attrs['class'] = 'form-control'
        self.fields['costo'].widget.attrs['placeholder'] = '$ 0.0'
        self.fields['costo'].error_messages['required'] = "Debes llenar este campo"
        self.fields['costo'].error_messages['invalid'] = "Debe ser un numero"
        self.fields['costo'].label = 'Precio de compra'
        self.fields['costo'].widget.attrs['ng-model'] = 'costo_input'
        self.fields['costo'].widget.attrs['autocomplete'] = 'off'
        self.fields['costo'].widget.attrs['ng-change'] = 'calcular_precio()'


        self.fields['porcentaje'].widget = forms.TextInput()
        self.fields['porcentaje'].initial = ""
        self.fields['porcentaje'].widget.attrs['class'] = 'form-control'
        self.fields['porcentaje'].widget.attrs['placeholder'] = '0%'
        self.fields['porcentaje'].error_messages['required'] = "Debes llenar este campo"
        self.fields['porcentaje'].error_messages['invalid'] = "Debe ser un numero"
        self.fields['porcentaje'].label = 'Porcentaje de ganancia por producto'
        self.fields['porcentaje'].widget.attrs['ng-model'] = 'porcentaje_input'
        self.fields['porcentaje'].widget.attrs['ng-change'] = 'calcular_precio()'
        self.fields['porcentaje'].widget.attrs['autocomplete'] = 'off'


        self.fields['codigo_barras'].widget = forms.TextInput()
        self.fields['codigo_barras'].widget.attrs['class'] = 'form-control'
        self.fields['codigo_barras'].widget.attrs['placeholder'] = '00000000000000'
        self.fields['codigo_barras'].initial = ''
        self.fields['codigo_barras'].error_messages['required'] = "Debes llenar este campo"
        self.fields['codigo_barras'].error_messages['invalid'] = "Debe ser un numero"

        self.fields['categoria'].error_messages['required'] = "Debes escoger una categoria"

        self.fields['numero_productos'].widget.attrs['class'] = 'form-control'
        self.fields['numero_productos'].widget.attrs['placeholder'] = 'Introduce un numero de productos a agregar'
        self.fields['numero_productos'].label = 'Numero de productos'
        self.fields['numero_productos'].error_messages['required'] = "Debes introducir un numero "
        self.fields['numero_productos'].initial = ""


class Cambiar_precio_form(forms.Form):
    producto = forms.ModelChoiceField(queryset = Articulo.objects.filter(sucursal=0),widget = forms.Select(attrs={'class':'form-control'}), label = 'Nombre del articulo' )
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
    producto = forms.ModelChoiceField(queryset = Articulo.objects.filter(sucursal=0),widget = forms.Select(attrs={'class':'form-control'}), label = 'Nombre del articulo a borrar' )

    def __init__(self,*args,**kwargs):
        super(borrar_producto_form,self).__init__(*args, **kwargs)
        self.fields['producto'].error_messages['required'] = "Debes escoger un articulo"
        self.fields['producto'].error_messages['invalid'] = "Debes cumplir con el formato"