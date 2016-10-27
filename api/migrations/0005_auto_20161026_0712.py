# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20161026_0449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='lasttimeminutes',
            new_name='lasttimeminute',
        ),
    ]
