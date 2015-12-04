# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0004_player_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='serialno',
            field=models.IntegerField(default=1),
        ),
    ]
