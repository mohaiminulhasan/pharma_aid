# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_remove_prescription_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='image',
            field=models.ImageField(blank=True, height_field='height', max_length=255, upload_to='uploads/prescription', width_field='width'),
        ),
    ]
