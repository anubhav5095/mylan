# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-13 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymedapp', '0002_auto_20181013_1240'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Medicine',
        ),
    ]