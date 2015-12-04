# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0017_auto_20150829_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='attack1_damage',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack2_damage',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack3_damage',
            field=models.IntegerField(default=40),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack4_damage',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='health',
            field=models.IntegerField(default=500),
        ),
    ]
