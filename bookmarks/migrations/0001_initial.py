# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('url', models.URLField(unique=True, verbose_name='url')),
                ('description', models.TextField(verbose_name='description')),
                ('extended', models.TextField(verbose_name='extended', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('tags', tagging.fields.TagField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'bookmarks',
                'verbose_name': 'bookmark',
                'verbose_name_plural': 'bookmarks',
            },
        ),
    ]
