# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='profession_name',
            new_name='professor_name',
        ),
    ]
