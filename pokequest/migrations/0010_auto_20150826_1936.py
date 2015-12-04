# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0009_player_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serialno', models.IntegerField(default=1)),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='puzzle1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='puzzle2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='puzzle3',
            field=models.IntegerField(default=0),
        ),
    ]
