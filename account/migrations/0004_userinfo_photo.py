# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-11 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userinfo_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
