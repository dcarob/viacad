# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-18 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viacadapp', '0013_auto_20171118_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='foto',
            field=models.ImageField(upload_to='viacadapp/profilephoto'),
        ),
    ]
