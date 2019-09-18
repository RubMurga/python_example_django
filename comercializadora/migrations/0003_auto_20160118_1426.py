# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comercializadora', '0002_auto_20160118_1425'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articulo',
            new_name='Articulo_comercializadora',
        ),
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Categoria_comercializadora',
        ),
    ]
