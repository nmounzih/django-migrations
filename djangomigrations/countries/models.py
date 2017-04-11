from django.db import models

# Create your models here.
class Countries(models.Model):
    name = models.CharField(max_length=200)
    capital = models.CharField(max_length=200)
    population = models.DecimalField(max_digits=10, decimal_places=5)
    aggregate = models.IntegerField(default=0)
    status = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    export = models.CharField(max_length=200)
