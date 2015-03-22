from django.db import models

class Comment(models.Model):
    user = models.CharField(max_length=100)
    comment = models.TextField()