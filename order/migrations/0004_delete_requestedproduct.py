# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20160809_1407'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RequestedProduct',
        ),
    ]