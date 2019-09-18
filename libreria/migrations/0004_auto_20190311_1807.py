# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_auto_20160904_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo_barras',
            field=models.CharField(max_length=150),
        ),
    ]
