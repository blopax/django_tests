from django.db import models

from .planets import Planets
# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=64, null=True)
    birth_year = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=32, null=True)
    eye_color = models.CharField(max_length=32, null=True)
    hair_color = models.CharField(max_length=32, null=True)
    height = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE, null=True)
    created = models.CharField(max_length=128, null=True)
    updated = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name    