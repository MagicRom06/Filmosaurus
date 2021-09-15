from django.core.management.base import BaseCommand
from .movie import Movie
from .category import CategoryToDB


class Command(BaseCommand):
    help = 'Populate the database'

    def handle(self, *args, **kwargs):
        csv = Movie.load()
        movies = Movie.parse(csv)
        self.insert_categories_to_db(movies)

    def insert_categories_to_db(self, movies_list):
        categories_list = list()
        for movie in movies_list:
            for category in movie.category.split(', '):
                categories_list.append(category)
        categories_list = list(set(categories_list))
        CategoryToDB.insert(categories_list)
