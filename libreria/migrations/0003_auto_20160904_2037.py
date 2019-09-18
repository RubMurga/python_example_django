# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_categoria_sucursal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='sucursal',
        ),
        migrations.AddField(
            model_name='articulo',
            name='sucursal',
            field=models.SmallIntegerField(default=0),
        ),
    ]
