# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 07:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('slug', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField()),
                ('title', models.CharField(max_length=64)),
                ('style', models.CharField(max_length=32)),
                ('thumbnail', models.ImageField(upload_to=b'')),
                ('image', models.ImageField(upload_to=b'')),
                ('image2', models.ImageField(upload_to=b'')),
                ('image3', models.ImageField(upload_to=b'')),
                ('image4', models.ImageField(upload_to=b'')),
                ('date', models.DateTimeField(default=datetime.datetime.utcnow, verbose_name='date published')),
                ('credit', models.CharField(max_length=128)),
                ('medium', models.CharField(max_length=128)),
                ('client', models.CharField(max_length=128)),
                ('client_url', models.URLField()),
                ('project', models.CharField(max_length=128)),
                ('project_url', models.URLField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='gallerypost',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Tag'),
        ),
    ]