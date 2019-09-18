# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comercializadora', '0004_categoria_comercializadora_sucursal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria_comercializadora',
            name='sucursal',
        ),
        migrations.AddField(
            model_name='articulo_comercializadora',
            name='sucursal',
            field=models.SmallIntegerField(default=0),
        ),
    ]
