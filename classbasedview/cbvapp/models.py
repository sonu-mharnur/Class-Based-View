
from django.db import models

# Create your models here.

class Comments(models.Model):
    comment = models.CharField('Comment', max_length=200)
    updatedat = models.DateTimeField('Updated At', auto_now=True)

    def __str__(self) -> str:
        return self.comment