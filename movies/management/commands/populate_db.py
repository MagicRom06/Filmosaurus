from django.core.management.base import BaseCommand
from .movie import Movie
from .category import CategoryToDB
from .country import CountryToDB
from .person import PersonToDB


class Command(BaseCommand):
    help = 'Populate the database'

    def handle(self, *args, **kwargs):
        csv = Movie.load()
        movies = Movie.parse(csv)
        # self.insert_categories_to_db(movies)
        # self.insert_countries_to_db(movies)
        # self.insert_cast_to_db(movies)

    def insert_categories_to_db(self, movies_list):
        categories_list = list()
        for movie in movies_list:
            for category in movie.category.split(', '):
                categories_list.append(category)
        categories_list = list(set(categories_list))
        CategoryToDB.insert(categories_list)

    def insert_countries_to_db(self, movies_list):
        countries_list = list()
        for movie in movies_list:
            for country in movie.country.split(', '):
                countries_list.append(country)
        countries_list = list(set(countries_list))
        CountryToDB.insert(countries_list)

    def insert_cast_to_db(self, movies_list):
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
