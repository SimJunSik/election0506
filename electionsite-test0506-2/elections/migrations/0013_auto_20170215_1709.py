# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 08:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0012_commitment_detail_commitment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commitment',
            old_name='detail_commitment',
            new_name='detail_cmmt',
        ),
    ]