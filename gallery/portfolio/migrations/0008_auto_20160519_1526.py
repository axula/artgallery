# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20160516_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='gallerypost',
            name='slug',
            field=models.SlugField(blank=True, max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, max_length=32, unique=True),
        ),
    ]