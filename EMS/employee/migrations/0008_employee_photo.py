# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-02 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20170428_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]