# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 16:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blogpage_sidebar_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postpage',
            old_name='header_image',
            new_name='sidebar_image',
        ),
    ]
