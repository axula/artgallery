# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20160513_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallerypost',
            name='url',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='url',
        ),
        migrations.AddField(
            model_name='gallerypost',
            name='slug',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.CharField(default='temp', max_length=32),
            preserve_default=False,
        ),
    ]
