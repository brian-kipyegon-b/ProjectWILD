from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100) #define a string width for animal
    age = models.IntegerField()
    dob = models.DateTimeField()
    species = models.CharField(max_length=200)
    bio = models.CharField(max_length=255)
    weight = models.FloatField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name