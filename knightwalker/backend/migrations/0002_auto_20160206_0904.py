# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='departure_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
