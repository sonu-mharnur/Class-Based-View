from django.db import models

# Create your models here.
class Empoyee(models.Model):
    eno = models.CharField("Emp No.",max_length=5)
    ename = models.CharField("Emp name",max_length=50)
    esal = models.CharField("Emp sal",max_length=10)

    def __str__(self) -> str:
        return self.ename