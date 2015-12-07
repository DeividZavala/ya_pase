# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_auto_20151207_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('numero', models.FloatField()),
                ('Vide_link', models.URLField()),
                ('curso_padre', models.ForeignKey(to='cursos.Curso')),
            ],
        ),
        migrations.DeleteModel(
            name='SubTema',
        ),
        migrations.AlterField(
            model_name='tema',
            name='subtemas',
            field=models.ManyToManyField(to='cursos.Clase', blank=True),
        ),
        migrations.AddField(
            model_name='clase',
            name='subtema_padre',
            field=models.ForeignKey(to='cursos.Tema'),
        ),
    ]
