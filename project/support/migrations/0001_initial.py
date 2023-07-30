# Generated by Django 3.2.20 on 2023-07-28 07:17

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
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('regTime', models.DateTimeField(verbose_name=datetime.datetime(2023, 7, 28, 7, 17, 3, 459168, tzinfo=utc))),
                ('deadline', models.DateTimeField()),
                ('fundraising', models.IntegerField()),
                ('account', models.CharField(max_length=14)),
                ('bank', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('진행중', 'in_progress'), ('완료', 'complete')], default='진행중', max_length=5)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.artist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupportForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depositor', models.CharField(max_length=10)),
                ('credit', models.IntegerField()),
                ('creditTime', models.DateTimeField()),
                ('status', models.CharField(choices=[('대기', 'waiting'), ('확인', 'auto_check'), ('취소', 'cancel')], default='대기', max_length=5)),
                ('support', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.support')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
