# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-24 09:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20160919_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
    ]