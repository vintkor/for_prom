# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='cart',
            field=models.ManyToManyField(to='cart.Cart', verbose_name='Корзина'),
        ),
    ]
