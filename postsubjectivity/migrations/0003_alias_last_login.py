# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 17:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postsubjectivity', '0002_answer_beat_question_textpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='alias',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 30, 17, 3, 7, 829195, tzinfo=utc), verbose_name='last log'),
            preserve_default=False,
        ),
    ]
