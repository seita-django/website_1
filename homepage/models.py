from django.db import models
from django.utils import timezone

# Create your models here.

""" Post Q and A from Admin page """
class Topic(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    text = models.TextField()

    def __str__(self):
        return self.title



