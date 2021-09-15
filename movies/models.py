from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)


class Person(models.Model):
    name = models.CharField(max_length=255)


class Country(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    picture = models.TextField()
    plot = models.TextField()
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Person, related_name='director')
    cast = models.ManyToManyField(Person, related_name='cast')
    country = models.ManyToManyField(Country)
