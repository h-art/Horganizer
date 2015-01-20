# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20150119_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='end_date',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='period',
            name='start_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
