# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 03:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import resume.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField()),
                ('degree', models.CharField(max_length=128)),
                ('school', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=64)),
                ('date', models.DateField(verbose_name='date')),
                ('description', tinymce.models.HTMLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField()),
                ('title', models.CharField(max_length=64)),
                ('company', models.CharField(max_length=64)),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('description', tinymce.models.HTMLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=64, unique=True)),
                ('job_title', models.CharField(blank=True, max_length=128)),
                ('image', models.ImageField(blank=True, upload_to=resume.models.PathAndRename('resume/'))),
                ('about', tinymce.models.HTMLField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('location', models.CharField(blank=True, max_length=64)),
                ('specializations', tinymce.models.HTMLField()),
                ('skills', tinymce.models.HTMLField()),
                ('tools', tinymce.models.HTMLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='resume.Resume'),
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='resume.Resume'),
        ),
    ]
