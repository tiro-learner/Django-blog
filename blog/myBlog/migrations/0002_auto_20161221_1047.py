# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 02:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleimage',
            name='article',
        ),
        migrations.DeleteModel(
            name='ArticleImage',
        ),
    ]
