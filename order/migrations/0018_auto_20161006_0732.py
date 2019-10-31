# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-06 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_auto_20160918_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, b'Submitted'), (2, b'Processed'), (3, b'Shipped'), (4, b'Cancelled'), (5, b'Returned')], default=1),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='image',
            field=models.ImageField(height_field=b'height', upload_to=b'img/prescription', width_field=b'width'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='thumbnail',
            field=models.ImageField(upload_to=b'img/prescription'),
        ),
    ]