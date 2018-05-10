from django.db import models

# Create your models here.


class Paste(models.Model):
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    content = models.TextField()