# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-05 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='key',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
