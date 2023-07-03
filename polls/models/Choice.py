from django.db import models
from polls.models.Question import Question


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.PROTECT)
    choice_text = models.TextField()

    def __str__(self):
        return self.choice_text
