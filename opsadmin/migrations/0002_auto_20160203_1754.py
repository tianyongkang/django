# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsadmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloudhost_config',
            name='name',
        ),
        migrations.DeleteModel(
            name='Cloudhost',
        ),
        migrations.DeleteModel(
            name='Cloudhost_config',
        ),
    ]
