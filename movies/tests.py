from movies.models import Movie, Category
from django.test import TestCase

# Create your tests here.


class MoviesTest(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            imdb_id=1001001,
            title='test title',
            year=1900,
            picture=None,
            plot='Plot TEST'
        )
        self.movie.category.add(
            Category.objects.create(name="test category"))

    def test_movie_listing(self):
        self.assertEqual(f"{self.movie.title}", 'test title')
        self.assertEqual(self.movie.imdb_id, 1001001)
        self.assertEqual(self.movie.year, 1900)
        self.assertEqual(f"{self.movie.plot}", 'Plot TEST')
        # self.assertEqual(f"{self.movie.category.name}", 'test category')
