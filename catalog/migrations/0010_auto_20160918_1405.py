# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-18 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20160825_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='generic',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Manufacturer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.CharField(blank=True, help_text='Content for description meta tag.', max_length=255, verbose_name='Meta Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(blank=True, help_text='Comma-delimited set of SEO keywords for meta tag.', max_length=255, verbose_name='Meta Keywords'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, help_text='Unique identifier for the product', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(blank=True, help_text='Unit used to sell the product, e.g. 250 gm, bottle, etc.', max_length=20, null=True),
        ),
    ]