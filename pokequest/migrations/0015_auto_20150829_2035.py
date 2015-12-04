# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0014_auto_20150829_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='attack2_name',
            field=models.CharField(default=b'attack2', max_length=200),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='attack3_name',
            field=models.CharField(default=b'attack3', max_length=200),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='attack4_name',
            field=models.CharField(default=b'attack4', max_length=200),
        ),
    ]
