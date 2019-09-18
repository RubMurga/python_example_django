# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('completed_data', models.SmallIntegerField(default=0)),
                ('belongs_to', models.CharField(max_length=100, choices=[(b'Cafeteria', b'Cafeteria'), (b'Libreria', b'Libreria')])),
                ('picture', models.ImageField(upload_to=b'imagenes_perfil', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
