# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EVS', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='mobno',
            new_name='mobile_number',
        ),
    ]
