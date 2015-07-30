# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quarter', '0003_auto_20150314_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
