# Generated by Django 3.2.20 on 2023-07-27 13:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0005_alter_alert_regtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='regTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 7, 27, 13, 52, 27, 527372, tzinfo=utc)),
        ),
    ]
