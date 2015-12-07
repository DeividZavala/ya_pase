# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_auto_20151207_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
