# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-03 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blocked',
            field=models.ManyToManyField(blank=True, to='search.Ingredient'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='saved',
            field=models.ManyToManyField(blank=True, to='search.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='search.Ingredient'),
        ),
    ]
