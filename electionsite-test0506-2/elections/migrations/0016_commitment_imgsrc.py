# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0015_auto_20170218_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='commitment',
            name='imgsrc',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
