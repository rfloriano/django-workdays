# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quarter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quarter',
            name='is_every_year',
        ),
    ]
