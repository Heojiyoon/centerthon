# Generated by Django 3.2.20 on 2023-07-30 13:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20230730_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='regTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 7, 30, 13, 49, 12, 976836, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='regTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 7, 30, 13, 49, 12, 975829, tzinfo=utc)),
        ),
    ]
