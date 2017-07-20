# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-07-18 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_auto_20170718_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='total',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='books',
            name='specifications',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
