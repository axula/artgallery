# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerypost',
            name='url',
            field=models.CharField(default='test', editable=False, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='url',
            field=models.CharField(default='test', editable=False, max_length=32),
            preserve_default=False,
        ),
    ]