from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.TextField()
    watcher = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)


    def __str__(self):
        return self.title