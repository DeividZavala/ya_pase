# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0011_auto_20151208_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='img',
            field=models.ImageField(null=True, upload_to='cursos', blank=True),
        ),
    ]
