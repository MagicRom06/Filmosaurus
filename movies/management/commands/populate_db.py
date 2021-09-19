from django.core.management.base import BaseCommand
from .movie import MovieToDB
from .category import CategoryToDB
from .country import CountryToDB
from .person import PersonToDB
from movies.models import Movie, Country, Category, Person


class Command(BaseCommand):
    help = 'Populate the database'

    def handle(self, *args, **kwargs):
        csv = MovieToDB.load()
        movies = MovieToDB.parse(csv)
        # self.insert_categories_to_db(movies)
        # self.insert_countries_to_db(movies)
        # self.insert_cast_to_db(movies)
        self.insert_movies_to_db(movies)

    def insert_movies_to_db(self, movies_list):
        """
        Insert movies with manytomany relation
        in DB
        """
        for movie in movies_list:
            print(movie.title)
            if Movie.objects.filter(
                title=movie.title,
                year=movie.year
            ).exists():
                print(f'{movie.title} exists')
            else:
                new_entry = Movie.objects.create(
                    title=movie.title,
                    year=movie.year,
                    picture=movie.picture,
                    plot=movie.plot
                )
                new_entry.save()
                for country in movie.country.split(', '):
                    new_entry.countries.add(Country.objects.get(name=country))
                for category in movie.category.split(', '):
                    new_entry.categories.add(
                        Category.objects.get(name=category))
                for director in movie.director.split(', '):
                    new_entry.directors.add(Person.objects.get(name=director))
                for actor in movie.cast.split(', '):
                    new_entry.casts.add(Person.objects.get(name=actor))

    def insert_categories_to_db(self, movies_list):
        """
        Insert categories on DB
        """
        categories_list = list()
        for movie in movies_list:
            for category in movie.category.split(', '):
                categories_list.append(category)
        categories_list = list(set(categories_list))
        CategoryToDB.insert(categories_list)

    def insert_countries_to_db(self, movies_list):
        """
        Insert countries on DB
        """
        countries_list = list()
        for movie in movies_list:
            for country in movie.country.split(', '):
                countries_list.append(country)
        countries_list = list(set(countries_list))
        CountryToDB.insert(countries_list)

    def insert_cast_to_db(self, movies_list):
        """
        Insert persons on DB
        """
        person_list = list()
        actor_list = list()
        director_list = list()
        for movie in movies_list:
            for director in movie.director.split(', '):
                director_list.append(director)
            for actors in movie.cast.split(', '):
                actor_list.append(actors)
        person_list = actor_list + director_list
        person_list = list(set(person_list))
        PersonToDB.insert(person_list)
