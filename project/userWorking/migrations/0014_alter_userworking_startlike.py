# Generated by Django 3.2.20 on 2023-07-30 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userWorking', '0013_alter_userworking_startlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userworking',
            name='startLike',
            field=models.DateField(verbose_name=datetime.datetime(2023, 7, 30, 8, 4, 30, 496062, tzinfo=utc)),
        ),
    ]
