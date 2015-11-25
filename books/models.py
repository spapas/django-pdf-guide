from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=64)
    abstract = models.CharField(max_length=256)
    cover = models.ImageField(max_length=64)

    