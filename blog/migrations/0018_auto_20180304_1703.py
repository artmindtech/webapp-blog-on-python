# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20180304_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='page_name_1',
            new_name='add_page_1',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='add_page_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='add_page_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='add_page_4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='add_page_5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='add_page_6',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='link_to_page_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='link_to_page_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='link_to_page_4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='link_to_page_5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='link_to_page_6',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
