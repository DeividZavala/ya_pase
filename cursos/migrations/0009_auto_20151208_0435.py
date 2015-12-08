# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0008_auto_20151207_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clase',
            old_name='Vide_link',
            new_name='video_link',
        ),
    ]
