# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0021_auto_20170227_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='idx',
        ),
        migrations.AddField(
            model_name='poll',
            name='id',
            field=models.AutoField(auto_created=True, default=int, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]