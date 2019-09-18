# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitacoraborrado',
            name='borrado_de',
            field=models.CharField(default=b'Ninguno', max_length=200),
        ),
    ]
