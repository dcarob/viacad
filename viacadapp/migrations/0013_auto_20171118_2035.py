# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-18 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viacadapp', '0012_auto_20171112_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsable', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=30)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Votaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreprofesor', models.CharField(max_length=80)),
                ('votacion', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AlterModelTable(
            name='materias',
            table='viacadapp_materias',
        ),
    ]
