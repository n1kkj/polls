# Generated by Django 4.2.2 on 2023-06-30 09:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0011_user_remove_answer_user_id_alter_poll_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_time',
            field=models.DateField(default=datetime.datetime(2023, 6, 30, 9, 26, 45, 492863)),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
