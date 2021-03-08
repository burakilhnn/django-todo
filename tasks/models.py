from django.db import models
from django.utils import timezone

class Tasks(models.Model):
    task = models.CharField(max_length=100)
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task
