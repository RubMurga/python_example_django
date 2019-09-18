# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='sucursal',
            field=models.SmallIntegerField(default=0),
        ),
    ]
