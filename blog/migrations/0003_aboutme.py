# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-02 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('interests_hobbies', models.TextField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
