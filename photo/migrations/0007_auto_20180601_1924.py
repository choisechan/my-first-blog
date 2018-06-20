# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-01 10:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import photo.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0006_merge_20180601_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.Album'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=photo.fields.ThumbnailImageField(upload_to='photo/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='origin',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
