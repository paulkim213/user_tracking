# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='target_ct',
            field=models.ForeignKey(null=True, to='contenttypes.ContentType', related_name='target_obj', blank=True),
        ),
        migrations.AddField(
            model_name='action',
            name='target_id',
            field=models.PositiveIntegerField(null=True, blank=True, db_index=True),
        ),
    ]
