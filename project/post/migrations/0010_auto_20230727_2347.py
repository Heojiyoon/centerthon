# Generated by Django 3.2.20 on 2023-07-27 14:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20230727_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='regTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 7, 27, 14, 47, 43, 761212, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='regTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 7, 27, 14, 47, 43, 761212, tzinfo=utc)),
        ),
    ]
