# Generated by Django 2.0.4 on 2018-08-26 12:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20180826_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 12, 15, 27, 507560, tzinfo=utc)),
        ),
    ]
