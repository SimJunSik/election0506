# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0009_commitment_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='ctname',
            field=models.CharField(default='df', max_length=20),
        ),
    ]