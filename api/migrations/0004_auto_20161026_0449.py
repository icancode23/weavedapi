# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_time_proxyadd1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='lasttime',
            new_name='lasttimehour',
        ),
        migrations.AddField(
            model_name='time',
            name='lasttimeminutes',
            field=models.BigIntegerField(null=True),
            preserve_default=True,
        ),
    ]
