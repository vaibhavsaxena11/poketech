# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('damage', models.IntegerField(default=0)),
                ('unlocked', models.BooleanField(default=False)),
                ('defensive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('absent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('health', models.IntegerField(default=100)),
                ('unlocked', models.BooleanField(default=False)),
                ('player', models.ForeignKey(to='pokequest.Player')),
            ],
        ),
        migrations.AddField(
            model_name='attack',
            name='poke',
            field=models.ForeignKey(to='pokequest.Pokemon'),
        ),
    ]
