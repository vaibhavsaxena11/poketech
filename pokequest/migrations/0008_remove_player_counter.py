# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0007_auto_20150826_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='counter',
        ),
    ]
