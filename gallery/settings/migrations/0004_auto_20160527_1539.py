# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_auto_20160527_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationlink',
            name='menu',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='links', to='settings.NavigationMenu'),
        ),
        migrations.AlterField(
            model_name='navigationlink',
            name='link',
            field=models.URLField(default='#'),
        ),
    ]
