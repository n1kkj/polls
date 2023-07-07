from django.db import models
from polls.models.question import Question


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.PROTECT)
    choice_text = models.CharField()

    def __str__(self):
        return self.choice_text
