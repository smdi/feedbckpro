# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-27 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rating', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.CharField(max_length=2000)),
            ],
        ),
    ]