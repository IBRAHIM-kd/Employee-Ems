# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-21 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=500)),
                ('job_title', models.CharField(max_length=100)),
                ('date_started', models.DateField(blank=True, null=True)),
                ('job_description', models.CharField(max_length=300)),
                ('photo', models.CharField(max_length=300)),
            ],
        ),
    ]
