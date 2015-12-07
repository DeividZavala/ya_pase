# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20151207_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema',
            name='subtemas',
            field=models.ManyToManyField(to='cursos.SubTema', blank=True),
        ),
    ]
