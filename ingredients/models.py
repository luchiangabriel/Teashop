
from django.db import models
from users.models import AuthUser
from distributors.models import Distributor


class Ingredient(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    active = models.BooleanField(default=1)

    def __int__(self):
        return {self.quantity}

    def __str__(self):
        return f"{self.name} -{self.description} - {self.quantity} - {self.distributor}"


class Logs_Ingredients(models.Model):

    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=15)
    url = models.CharField(max_length=100)
