# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comercializadora', '0003_auto_20160118_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria_comercializadora',
            name='sucursal',
            field=models.SmallIntegerField(default=0),
        ),
    ]
