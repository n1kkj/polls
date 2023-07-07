from django.contrib.auth.models import User
from django.db import models
from polls.models.choice import Choice
from polls.models.question import Question


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='question', on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT, null=True)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.PROTECT, null=True)
    answer_text = models.CharField()

    def __str__(self):
        return self.answer_text
