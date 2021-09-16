import uuid
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    imdb_id = models.PositiveIntegerField(default=None)
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    picture = models.TextField(null=True)
    plot = models.TextField()
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Person, related_name='director')
    cast = models.ManyToManyField(Person, related_name='cast')
    country = models.ManyToManyField(Country)

    def __str__(self):
        return self.title
