# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-15 05:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_auto_20170115_0456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('crm_table_list', '可以访问 kingadmin 每个表的数据列表页'), ('crm_table_index', '可以访问 kingadmin 首页'), ('crm_table_list_view', '可以访问 kingadmin 每个表中对象的修改页'), ('crm_table_list_chnange', '可以修改 kingadmin 每个表中对象')), 'verbose_name': 'CRM账户', 'verbose_name_plural': 'CRM账户'},
        ),
    ]
