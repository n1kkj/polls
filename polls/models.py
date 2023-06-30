import datetime

from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    poll_title = models.CharField(max_length=4096)
    start_time = models.DateField(default=datetime.datetime.today())
    end_time = models.DateField(null=True)
    poll_description = models.CharField(max_length=4096)

    def __str__(self):
           return self.poll_title


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=4096)
    question_type = models.CharField(max_length=4096)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, related_name='poll', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE, null=True)
    answer_text = models.CharField(max_length=4096)

    def __str__(self):
        return self.answer_text
