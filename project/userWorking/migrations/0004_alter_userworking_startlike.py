# Generated by Django 3.2.20 on 2023-07-27 12:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userWorking', '0003_alter_userworking_startlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userworking',
            name='startLike',
            field=models.DateField(verbose_name=datetime.datetime(2023, 7, 27, 12, 3, 22, 116918, tzinfo=utc)),
        ),
    ]
