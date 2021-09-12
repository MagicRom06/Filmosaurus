from django.core.management.base import BaseCommand
from .movie import Movie


class Command(BaseCommand):
    help = 'Populate the database'

    def handle(self, *args, **kwargs):
        csv = Movie.load()
        Movie.parse(csv)
