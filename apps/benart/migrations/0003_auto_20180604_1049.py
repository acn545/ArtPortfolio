# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-04 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benart', '0002_art3d_drawings_gameart_paintings'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('user_level', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='art3d',
        ),
        migrations.DeleteModel(
            name='drawings',
        ),
        migrations.DeleteModel(
            name='gameArt',
        ),
        migrations.DeleteModel(
            name='paintings',
        ),
        migrations.AddField(
            model_name='images',
            name='type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='images',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='benart.images'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='benart.user'),
        ),
    ]
