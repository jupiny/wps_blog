# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpsblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaverPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('thumbnail_image_url', models.URLField()),
                ('original_url', models.URLField()),
            ],
        ),
    ]
