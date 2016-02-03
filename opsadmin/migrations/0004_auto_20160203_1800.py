# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsadmin', '0003_auto_20160203_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudhost',
            name='outip',
            field=models.GenericIPAddressField(verbose_name=True),
        ),
    ]
