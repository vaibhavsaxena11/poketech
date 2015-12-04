# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0010_auto_20150826_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='puzzle1',
            new_name='score',
        ),
        migrations.RemoveField(
            model_name='player',
            name='puzzle2',
        ),
        migrations.RemoveField(
            model_name='player',
            name='puzzle3',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack1mult',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack2mult',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack3mult',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='attack4mult',
        ),
    ]
