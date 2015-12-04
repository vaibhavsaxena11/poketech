# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0019_delete_attack'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Puzzle',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack4',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack4_damage',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack4_name',
        ),
    ]
