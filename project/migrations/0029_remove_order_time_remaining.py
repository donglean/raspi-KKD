# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 16:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0028_auto_20170313_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='time_remaining',
        ),
    ]