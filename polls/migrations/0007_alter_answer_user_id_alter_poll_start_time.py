# Generated by Django 4.2.2 on 2023-06-27 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_poll_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_time',
            field=models.DateField(default=datetime.datetime(2023, 6, 27, 23, 17, 53, 409215)),
        ),
    ]