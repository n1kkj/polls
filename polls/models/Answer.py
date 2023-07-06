from django.contrib.auth.models import User
from django.db import models
from polls.models.Question import Question
from polls.models.Choice import Choice


class Answer(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT, null=True)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.PROTECT)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.PROTECT, null=True)
    answer_text = models.CharField()

    def __str__(self):
        return self.answer_text
