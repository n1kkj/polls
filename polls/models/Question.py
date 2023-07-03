from django.db import models
from polls.models.Poll import Poll


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.PROTECT)
    question_text = models.TextField()
    question_type = models.TextField()

    def __str__(self):
        return self.question_text
