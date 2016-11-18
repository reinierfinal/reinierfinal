# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('isbn', models.CharField(max_length=13)),
                ('titulo', models.CharField(max_length=60)),
                ('portada', models.CharField(max_length=13)),
                ('autor', models.CharField(max_length=100)),
                ('editoria', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='prestamo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('fechaprestamo', models.DateField()),
                ('fechadevp', models.DateField()),
                ('fechadevr', models.DateField()),
                ('tlibro', models.ForeignKey(to='examen.libro')),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dpi', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('libros', models.ManyToManyField(to='examen.libro', through='examen.prestamo')),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='tusuario',
            field=models.ForeignKey(to='examen.usuario'),
        ),
    ]
