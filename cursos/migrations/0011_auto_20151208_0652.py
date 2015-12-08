# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0010_clase_curso_padre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='curso_padre',
            field=models.ManyToManyField(blank=True, to='cursos.Curso'),
        ),
    ]
