# Generated by Django 2.0.4 on 2018-08-27 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_auto_20180826_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefprofile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 27, 18, 53, 10, 663102, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 27, 18, 53, 10, 665103, tzinfo=utc)),
        ),
    ]
