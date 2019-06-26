# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-12 05:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_auto_20161007_0445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dosage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='dosage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Dosage'),
        ),
    ]
