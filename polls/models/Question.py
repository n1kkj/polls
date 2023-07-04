from django.db import models
from polls.models.Poll import Poll
from polls.models.QuestionType import QuestionType


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.PROTECT)
    question_text = models.TextField()
    question_type = models.ForeignKey(QuestionType, related_name='question_type', on_delete=models.PROTECT)

    def __str__(self):
        return self.question_text
