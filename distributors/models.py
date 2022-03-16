
from django.db import models
from users.models import AuthUser


class Distributor(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.telephone}"


class Logs_Distributors(models.Model):

    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=15)
    url = models.CharField(max_length=100)
