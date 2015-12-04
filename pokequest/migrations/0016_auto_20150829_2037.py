# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0015_auto_20150829_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='attack1_name',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack2_name',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack3_name',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack4_name',
        ),
    ]
