# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20170525_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotional_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Preço promocional'),
        ),
    ]