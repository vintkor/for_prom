# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20170723_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cart',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.Cart', verbose_name='Корзина'),
        ),
    ]
