# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_auto_20151207_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='temas',
            field=models.ManyToManyField(blank=True, to='cursos.Tema'),
        ),
    ]
