# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_remove_resume_tools'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='still_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
