# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-01 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0011_auto_20180602_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.Album'),
        ),
    ]
