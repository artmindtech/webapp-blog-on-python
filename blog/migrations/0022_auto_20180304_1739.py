# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 14:39
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20180304_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('two_columns', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), icon='arrow-right', label='Left column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), icon='arrow-right', label='Right column content'))))), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('nav_link_title', wagtail.wagtailcore.blocks.CharBlock()), ('nav_link_url', wagtail.wagtailcore.blocks.CharBlock())), blank=True, null=True),
        ),
    ]
