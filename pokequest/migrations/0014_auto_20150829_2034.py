# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0013_pokemon_attack1_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='attack2_name',
            field=models.CharField(default=b'attack1', max_length=200),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack3_name',
            field=models.CharField(default=b'attack1', max_length=200),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack4_name',
            field=models.CharField(default=b'attack1', max_length=200),
        ),
    ]
