# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0002_articulo_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='codigo_barras',
            field=models.CharField(max_length=150),
        ),
    ]
