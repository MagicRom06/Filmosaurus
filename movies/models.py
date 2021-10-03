from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE
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
    user = models.ForeignKey(
        get_user_model(),
        on_delete=CASCADE,
        related_name='user',
        default=None
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=CASCADE,
        related_name='movie',
        default=None
    )
    seen = models.BooleanField(default=False)
    viewed_date = models.DateTimeField(null=True, blank=True)
    saved_date = models.DateTimeField(default=None)
