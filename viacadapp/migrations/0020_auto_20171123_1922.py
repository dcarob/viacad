# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-23 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viacadapp', '0019_auto_20171120_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesores',
            name='correo',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
