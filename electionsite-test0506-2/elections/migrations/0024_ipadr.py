# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0023_hitcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAdr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adr', models.CharField(max_length=100)),
            ],
        ),
    ]