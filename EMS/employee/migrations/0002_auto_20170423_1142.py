# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-23 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
