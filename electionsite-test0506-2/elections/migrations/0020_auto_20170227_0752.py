# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0019_commitment_imgsrc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='area',
        ),
        migrations.AddField(
            model_name='poll',
            name='idx',
            field=models.IntegerField(default=1),
        ),
    ]
