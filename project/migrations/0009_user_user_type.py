# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-11 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20170311_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.BooleanField(default=True),
        ),
    ]