# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-30 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20160927_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='related',
            field=models.ManyToManyField(related_name='_product_related_+', to='catalog.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='dosage',
            field=models.PositiveIntegerField(choices=[(1, 'Tablet'), (2, 'Capsule'), (3, 'Suppository'), (4, 'Syrup'), (5, 'Suspension'), (6, 'Injection (IV)'), (7, 'Injection (IM)'), (8, 'Contraceptive'), (9, 'Sanitary Napkin'), (10, 'Cream'), (11, 'Ointment'), (12, '')], default=1),
        ),
    ]
