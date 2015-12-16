# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0012_auto_20151211_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='author',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
