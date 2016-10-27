# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_time_proxyadd1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='proxyadd1',
        ),
    ]
