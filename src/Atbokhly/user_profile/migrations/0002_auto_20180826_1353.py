# Generated by Django 2.0.4 on 2018-08-26 10:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 10, 53, 50, 543649, tzinfo=utc)),
        ),
    ]