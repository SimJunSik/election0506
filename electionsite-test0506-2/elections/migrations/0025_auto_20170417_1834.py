# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0024_ipadr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commitment',
            name='ref',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
