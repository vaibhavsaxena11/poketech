# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attack',
            name='poke',
        ),
        migrations.RemoveField(
            model_name='attack',
            name='unlocked',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack1mult',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack2mult',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack3mult',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack4mult',
            field=models.IntegerField(default=1),
        ),
    ]
