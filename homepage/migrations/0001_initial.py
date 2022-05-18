# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('course_name', models.CharField(max_length=100)),
                ('profession_name', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('classroom', models.CharField(max_length=100)),
            ],
        ),
    ]
