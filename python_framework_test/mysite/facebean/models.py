import datetime

from django.db import models
from django.utils import timezone

class Message(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")
    username = models.CharField(max_length=100)
    avatar = models.CharField(max_length=200)
    def __str__(self):
        return self.content
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)
