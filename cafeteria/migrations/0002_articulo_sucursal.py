# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='sucursal',
            field=models.SmallIntegerField(default=0),
        ),
    ]
