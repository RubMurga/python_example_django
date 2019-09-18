# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comercializadora', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto_comercializadora',
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
                ('categoria', models.ForeignKey(to='comercializadora.Categoria')),
                ('nombre_articulo', models.ForeignKey(to='comercializadora.Articulo')),
                ('vendido_por', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='nombre_articulo',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
