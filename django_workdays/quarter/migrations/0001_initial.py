# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'name')),
                ('is_done', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Goal',
                'verbose_name_plural': 'Goals',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'name')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('is_every_year', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Quarter',
                'verbose_name_plural': 'Quarter',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='goal',
            name='quarter',
            field=models.ForeignKey(to='quarter.Quarter'),
            preserve_default=True,
        ),
    ]
