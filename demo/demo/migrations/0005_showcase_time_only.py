# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_showcase_readonly_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='showcase',
            name='time_only',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
