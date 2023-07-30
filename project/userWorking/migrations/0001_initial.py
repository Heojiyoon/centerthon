# Generated by Django 3.2.20 on 2023-07-28 07:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWorking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startLike', models.DateField(verbose_name=datetime.datetime(2023, 7, 28, 7, 6, 54, 369308, tzinfo=utc))),
                ('postRecord', models.IntegerField(default=0)),
                ('commentRecord', models.IntegerField(default=0)),
                ('meetingHost', models.IntegerField(default=0)),
                ('meetingGuest', models.IntegerField(default=0)),
                ('supportHost', models.IntegerField(default=0)),
                ('supportGuest', models.IntegerField(default=0)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.artist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
