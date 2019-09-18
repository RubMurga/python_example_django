# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='belongs_to',
            field=models.CharField(max_length=100, choices=[(b'Cafeteria', b'Cafeteria'), (b'Libreria', b'Libreria'), (b'Administrador', b'Administrador')]),
        ),
    ]
