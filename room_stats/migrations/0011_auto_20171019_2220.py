# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 22:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_stats', '0010_room_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
