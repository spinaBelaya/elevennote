from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    owner = models.ForeignKey(User, related_name = 'notes', on_delete = models.CASCADE, blank=True, null = True)


    def __str__(self):
        return self.title

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - timezone.timedelta(days=1)
        

