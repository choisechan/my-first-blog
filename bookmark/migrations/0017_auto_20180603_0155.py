# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0016_auto_20180602_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='price',
            field=models.CharField(blank=True, default='500', max_length=100, null=True),
        ),
    ]