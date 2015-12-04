# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0005_player_serialno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='progress',
            new_name='counter',
        ),
    ]
