from django.db import models
import datetime


class Poll(models.Model):
    poll_title = models.CharField(max_length=100)
    start_time = models.DateField(default=datetime.date.today)
    end_time = models.DateField(null=True)
    poll_description = models.TextField()

    def __str__(self):
        return self.poll_title
