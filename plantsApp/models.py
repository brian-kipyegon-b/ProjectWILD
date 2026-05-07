from django.db import models


# Create your models here.

class Car(models.Model):
    fuel_type = {
        "D":"Diesel",
        "P":"Petrol"
    }
    name = models.CharField(max_length=100)
    yop = models.IntegerField()
    description = models.CharField(max_length=250)
    fueltype = models.CharField(max_length=1, choices = fuel_type) 
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name