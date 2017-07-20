# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-07-17 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_router'),
    ]

    operations = [
        migrations.DeleteModel(
            name='router',
        ),
        migrations.AddField(
            model_name='books',
            name='specifications',
            field=models.FileField(null=True, upload_to='books_specifications'),
        ),
    ]
