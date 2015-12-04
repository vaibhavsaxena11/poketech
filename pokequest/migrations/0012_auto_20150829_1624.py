# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokequest', '0011_auto_20150829_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='absent',
            new_name='present',
        ),
    ]
