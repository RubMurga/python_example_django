# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('imagen', models.ImageField(upload_to=b'imagenes_libros', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_categoria', models.CharField(default=b'categoria', max_length=200)),
                ('slug', models.SlugField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_barras', models.BigIntegerField()),
                ('costo', models.DecimalField(default=0.0, max_digits=15, decimal_places=2)),
                ('precio', models.DecimalField(default=0.0, max_digits=15, decimal_places=2)),
                ('vendido', models.IntegerField(default=0)),
                ('en_caja', models.IntegerField(default=0, null=True, blank=True)),
                ('agregado_el_anio', models.IntegerField(default=0)),
                ('agregado_el_mes', models.IntegerField(default=0)),
                ('agregado_el_dia', models.IntegerField(default=0)),
                ('vendido_el_anio', models.IntegerField(default=0, null=True, blank=True)),
                ('vendido_el_mes', models.IntegerField(default=0, null=True, blank=True)),
                ('vendido_el_dia', models.IntegerField(default=0, null=True, blank=True)),
                ('categoria', models.ForeignKey(to='libreria.Categoria')),
                ('nombre_libro', models.ForeignKey(to='libreria.Articulo')),
                ('vendido_por', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
