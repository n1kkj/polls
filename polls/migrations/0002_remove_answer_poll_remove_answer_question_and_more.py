# Generated by Django 4.2.2 on 2023-06-26 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.RemoveField(
            model_name='question',
            name='poll',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
