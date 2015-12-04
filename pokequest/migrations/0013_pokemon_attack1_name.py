# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0012_auto_20150829_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='attack1_name',
            field=models.CharField(default=b'attack1', max_length=200),
        ),
    ]
