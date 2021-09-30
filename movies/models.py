from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

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
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    picture = models.TextField(null=True)
    plot = models.TextField()
    categories = models.ManyToManyField(Category)
    directors = models.ManyToManyField(Person, related_name='director')
    casts = models.ManyToManyField(Person, related_name='cast')
    countries = models.ManyToManyField(Country)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])


class Watchlist(models.Model):
    users = models.ManyToManyField(get_user_model())
    movies = models.ManyToManyField(Movie)
    seen = models.BooleanField(default=False)
