# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20150825_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sucursal',
            field=models.SmallIntegerField(default=0),
        ),
    ]
