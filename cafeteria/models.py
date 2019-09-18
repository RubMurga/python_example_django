from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Articulo(models.Model):
    nombre = models.CharField(blank = False, max_length = 200)
    slug = models.SlugField(unique = True)
    sucursal =models.SmallIntegerField(default = 0)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.nombre)
        super(Articulo,self).save(*args,**kwargs)

    def __unicode__(self):
        return self.nombre

class productos(models.Model):
    codigo_barras = models.CharField(null = False, blank = False, max_length = 150)
    nombre_producto = models.ForeignKey(Articulo)
    vendido = models.IntegerField(default = 0)
    en_caja = models.IntegerField(default = 0, blank = True, null = True)
    costo = models.DecimalField(default = 0.0, blank = False, max_digits = 15, decimal_places=2)
    precio = models.DecimalField(default = 0.0,max_digits=15, decimal_places=2)
    vendido_por = models.ForeignKey(User, blank = True,null = True)
    agregado_el_anio = models.IntegerField(default = 0)
    agregado_el_mes = models.IntegerField(default = 0)
    agregado_el_dia = models.IntegerField(default = 0)
    vendido_el_anio = models.IntegerField(blank = True, null = True,default = 0)
    vendido_el_mes = models.IntegerField(blank = True, null = True,default = 0)
    vendido_el_dia = models.IntegerField(blank = True, null = True,default = 0)
