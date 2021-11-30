from django.db import models
from django.db.models.fields import IntegerField
# Create your models here.

class Registration(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(default='')
    Password = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.Name