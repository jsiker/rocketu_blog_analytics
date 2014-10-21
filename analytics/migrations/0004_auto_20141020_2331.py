# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20141020_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='location',
            field=models.ForeignKey(blank=True, to='analytics.Location', null=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='page',
            field=models.ForeignKey(to='analytics.Page'),
        ),
    ]
