from django.db import models

# Create your models here.

from django.db import models


class BitacoraBorrado(models.Model):
    fecha = models.DateField(auto_now=True)
    costo = models.DecimalField(default = 0.0, blank = False, max_digits = 15, decimal_places=2)
    precio = models.DecimalField(default = 0.0,max_digits=15, decimal_places=2)
    nombre = models.CharField(blank = False, max_length = 200)
    numero = models.IntegerField(default = 0, blank = True, null = True)
    borrado_de = models.CharField(blank = False, max_length = 200, default = 'Ninguno')


