# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20170702_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='tag_list',
            field=models.ManyToManyField(blank=True, to='posts.Tag'),
        ),
    ]
