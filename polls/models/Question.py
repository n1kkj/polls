from django.db import models
from polls.models import Poll


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.TextField()

    def __str__(self):
        return self.question_text