# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_auto_20151207_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clase',
            name='curso_padre',
        ),
        migrations.RemoveField(
            model_name='clase',
            name='subtema_padre',
        ),
        migrations.RemoveField(
            model_name='tema',
            name='curso_padre',
        ),
    ]
