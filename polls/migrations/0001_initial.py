# Generated by Django 4.2.3 on 2023-07-07 21:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_title', models.CharField(max_length=100)),
                ('start_time', models.DateField(default=datetime.date.today)),
                ('end_time', models.DateField(null=True)),
                ('poll_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_type', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('answers', models.ManyToManyField(to='polls.answer')),
                ('choices', models.ManyToManyField(to='polls.choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='polls.poll')),
                ('question_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='question_type', to='polls.questiontype')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='choice', to='polls.choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
