# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-17 16:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0033_order_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_note',
            name='edited_by',
        ),
        migrations.RemoveField(
            model_name='order_note',
            name='last_modified',
        ),
    ]