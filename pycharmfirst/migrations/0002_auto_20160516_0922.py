# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pycharmfirst', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categoty',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pycharmfirst.Category'),
            preserve_default=False,
        ),
    ]
