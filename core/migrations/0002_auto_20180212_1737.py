# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-12 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, default=b'0.00', verbose_name=b'Price of Product'),
        ),
    ]
