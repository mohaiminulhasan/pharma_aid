# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-24 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20160818_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
