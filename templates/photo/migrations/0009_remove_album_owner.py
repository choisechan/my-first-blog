# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0008_album_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='owner',
        ),
    ]