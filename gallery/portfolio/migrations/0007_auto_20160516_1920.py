# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 02:20
from __future__ import unicode_literals

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20160516_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to=portfolio.models.PathAndRename('portfolio/')),
        ),
        migrations.AlterField(
            model_name='gallerypost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=portfolio.models.PathAndRename('portfolio/thumbnails/')),
        ),
    ]
