# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0020_auto_20150902_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='health',
            field=models.IntegerField(default=100),
        ),
    ]
