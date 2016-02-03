# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloudhost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('ip', models.IPAddressField()),
                ('date', models.DateField()),
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
                ('name', models.ForeignKey(to='opsadmin.Cloudhost')),
            ],
        ),
    ]
