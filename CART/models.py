from django.db import models
from HOME.models import *
from USER.models import *

# Create your models here.

class Mycart(models.Model):
    person = models.ForeignKey(Registration, on_delete=models.CASCADE)
    product = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True, null=True)
    update_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.person.Name

class Order(models.Model):
    order_id = models.PositiveIntegerField(default='')
    person = models.ForeignKey(Registration,on_delete=models.CASCADE)
    no_of_services = models.CharField(max_length=100)
    order_amount = models.CharField(max_length=80)
    ordered_on = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return self.person.Name
