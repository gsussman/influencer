# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-16 02:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
