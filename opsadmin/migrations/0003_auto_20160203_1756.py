# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsadmin', '0002_auto_20160203_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloudhost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.CharField(max_length=100)),
                ('intip', models.GenericIPAddressField()),
                ('outip', models.GenericIPAddressField()),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('createdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Cloudhost_config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpu', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('disk', models.IntegerField()),
                ('area', models.CharField(max_length=100)),
                ('bandwidth', models.IntegerField()),
                ('operateos', models.CharField(max_length=100)),
                ('hostid', models.ForeignKey(to='opsadmin.Cloudhost')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('developer', models.CharField(max_length=300)),
                ('manager', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='cloudhost',
            name='itemid',
            field=models.ForeignKey(to='opsadmin.Item'),
        ),
    ]
