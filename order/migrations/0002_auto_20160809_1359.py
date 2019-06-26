# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('group', models.CharField(blank=True, max_length=100)),
                ('power', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address_1',
            field=models.CharField(max_length=50, verbose_name='Line 1'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address_2',
            field=models.CharField(blank=True, max_length=50, verbose_name='Line 2'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_city',
            field=models.CharField(max_length=50, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_country',
            field=models.CharField(max_length=50, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_name',
            field=models.CharField(max_length=50, verbose_name='Recipient Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_zip',
            field=models.CharField(max_length=10, verbose_name='Zip Code'),
        ),
    ]
