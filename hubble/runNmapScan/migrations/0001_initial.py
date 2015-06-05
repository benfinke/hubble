# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scan_string', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Scan_results',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scan_live_hosts', models.IntegerField(default=0)),
                ('scan_output', models.CharField(max_length=10000)),
                ('scan_string', models.ForeignKey(to='runNmapScan.Scan')),
            ],
        ),
    ]
