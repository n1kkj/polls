from django.contrib.auth.models import User
from django.db import models
from polls.models import Question, Poll, Choice


class Answer(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, related_name='poll', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE, null=True)
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text
