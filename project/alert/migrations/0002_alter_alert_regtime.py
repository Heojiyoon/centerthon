# Generated by Django 3.2.20 on 2023-07-27 10:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='regTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 7, 27, 10, 59, 36, 833479, tzinfo=utc)),
        ),
    ]
