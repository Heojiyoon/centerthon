# Generated by Django 3.2.20 on 2023-07-30 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20230728_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='regTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 7, 30, 8, 4, 30, 493732, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='regTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 7, 30, 8, 4, 30, 493732, tzinfo=utc)),
        ),
    ]
