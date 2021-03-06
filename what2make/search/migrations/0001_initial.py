# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-12 01:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ing_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cost', models.PositiveSmallIntegerField()),
                ('ing_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Ing_Type')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocked', models.ManyToManyField(to='search.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='search.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('ingredients', models.ManyToManyField(to='search.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='recipe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='search.Recipe'),
        ),
        migrations.AddField(
            model_name='profile',
            name='saved',
            field=models.ManyToManyField(to='search.Recipe'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
