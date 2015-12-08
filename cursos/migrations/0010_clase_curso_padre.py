# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0009_auto_20151208_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='curso_padre',
            field=models.ManyToManyField(to='cursos.Curso'),
        ),
    ]
