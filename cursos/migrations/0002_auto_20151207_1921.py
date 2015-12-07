# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('numero', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='curso',
            name='descripcion',
            field=models.CharField(max_length=150),
        ),
        migrations.AddField(
            model_name='tema',
            name='curso_padre',
            field=models.ForeignKey(to='cursos.Curso'),
        ),
        migrations.AddField(
            model_name='tema',
            name='subtemas',
            field=models.ManyToManyField(to='cursos.SubTema'),
        ),
    ]
