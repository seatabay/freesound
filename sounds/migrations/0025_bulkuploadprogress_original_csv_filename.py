# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0024_merge_20180403_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkuploadprogress',
            name='original_csv_filename',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]