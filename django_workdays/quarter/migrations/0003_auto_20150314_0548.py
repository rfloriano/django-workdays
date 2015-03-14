# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quarter', '0002_remove_quarter_is_every_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'name'),
            preserve_default=True,
        ),
    ]
