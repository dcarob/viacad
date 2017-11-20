# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-20 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viacadapp', '0018_auto_20171120_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrecompleto', models.CharField(max_length=80)),
                ('correo', models.EmailField(max_length=100)),
                ('contraseña', models.CharField(max_length=32)),
                ('foto', models.ImageField(upload_to='viacadapp/images')),
                ('materia', models.CharField(max_length=250)),
                ('cualidades', models.CharField(max_length=250)),
                ('costohora', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
    ]