# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0004_auto_20141020_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='page',
            field=models.ForeignKey(related_name=b'views', to='analytics.Page'),
        ),
    ]
