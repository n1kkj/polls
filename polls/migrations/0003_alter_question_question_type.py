# Generated by Django 4.2.3 on 2023-07-04 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_questiontype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='question_type', to='polls.questiontype'),
        ),
    ]
