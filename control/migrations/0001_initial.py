# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitacoraBorrado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True)),
                ('costo', models.DecimalField(default=0.0, max_digits=15, decimal_places=2)),
                ('precio', models.DecimalField(default=0.0, max_digits=15, decimal_places=2)),
                ('nombre', models.CharField(max_length=200)),
                ('numero', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
    ]
