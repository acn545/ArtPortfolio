# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-04 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benart', '0003_auto_20180604_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='allimg',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
