# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0006_auto_20150826_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='counter',
            field=models.IntegerField(default=1),
        ),
    ]
