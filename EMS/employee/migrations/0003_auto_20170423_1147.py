# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-23 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20170423_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to=b''),
        ),
    ]
