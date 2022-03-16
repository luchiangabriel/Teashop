
from django.db import models
from users.models import AuthUser
from ingredients.models import Ingredient
from utils.photo_resize import make_thumbnail


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    quantity = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.name} -{self.ingredients} - {self.image} - {self.quantity}"

    def save(self, *args, **kwargs):
        self.image = make_thumbnail(self.image, size=(100, 100))
        super().save(*args, **kwargs)


class Logs_Recipes(models.Model):

    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=15)
    url = models.CharField(max_length=100)
