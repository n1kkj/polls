from django.db import models


class QuestionType(models.Model):
    q_type = models.CharField()

    def __str__(self):
        return self.q_type
