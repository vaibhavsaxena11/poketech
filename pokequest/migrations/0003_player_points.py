# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0002_auto_20150823_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
