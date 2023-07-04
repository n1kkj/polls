from django.db import models


class QuestionType(models.Model):
    type = models.TextField()

    def __str__(self):
        return self.type
