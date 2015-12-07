# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_curso_temas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='descripcion',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descripcion',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='tema',
            name='descripcion',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
