from django.db import models

# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name

class Service(models.Model):
    Service_Name = models.CharField(max_length=40)
    Price = models.IntegerField(default='')
    Image = models.ImageField(upload_to= 'new_img', blank = True) 

    def __str__(self) -> str:
        return self.Service_Name