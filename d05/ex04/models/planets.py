from django.db import models

# Create your models here.

class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    climate = models.TextField(null=True)
    diameter = models.IntegerField(null=True)
    orbital_period = models.IntegerField(null=True)
    population = models.BigIntegerField(null=True)
    rotation_period = models.IntegerField(null=True)
    surface_water = models.FloatField(null=True)
    terrain = models.TextField(null=True)
    created = models.CharField(max_length=128, null=True)
    updated = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name