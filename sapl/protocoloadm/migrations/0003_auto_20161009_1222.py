# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-09 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocoloadm', '0002_delete_tipoinstituicao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentoadministrativo',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Autor'),
        ),
        migrations.AlterField(
            model_name='protocolo',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Autor'),
        ),
    ]