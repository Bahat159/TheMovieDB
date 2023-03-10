
from django.db import models

# Create your models here.

class ListItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    language = models.TextField()

    def __str__(self):
        return self.name
