# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0008_auto_20170213_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='commitment',
            name='index',
            field=models.IntegerField(default=0),
        ),
    ]
