# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpsblog', '0002_naverpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='keyword',
            field=models.CharField(default='기록없음', max_length=16),
            preserve_default=False,
        ),
    ]
