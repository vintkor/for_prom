# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_remove_condition_product'),
        ('catalog', '0004_auto_20170807_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogproduct',
            name='condition',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='information.Condition', verbose_name='Условия поставщика'),
        ),
    ]
