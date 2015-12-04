# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0003_player_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]
