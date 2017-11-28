# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('createTime', models.DateTimeField(verbose_name='create time')),
                ('updateTime', models.DateTimeField(verbose_name='update time')),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
