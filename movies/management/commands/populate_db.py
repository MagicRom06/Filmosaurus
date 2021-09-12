from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populate the database'

    def handle(self, *args, **kwargs):
        print('hello world')
