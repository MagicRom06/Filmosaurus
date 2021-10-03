from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from movies.models import Category, Country, Movie, Person, Watchlist

# Create your tests here.


class MoviesTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test username',
            email="test@test.com",
            password="test1234"
        )
        self.movie = Movie.objects.create(
            title='The matrix',
            year=1999,
            picture=None,
            plot='Plot TEST'
        )
        self.movie.categories.add(
            Category.objects.create(name="test category"))

        self.movie.countries.add(
            Country.objects.create(name="test country"))

        self.movie.directors.add(
            Person.objects.create(name="test director"))

        self.movie.casts.add(
            Person.objects.create(name="test cast"))

    def test_movie_listing(self):
        self.assertEqual(f"{self.movie.title}", 'The matrix')
        self.assertEqual(self.movie.year, 1999)
        self.assertEqual(f"{self.movie.plot}", 'Plot TEST')
        self.assertEqual(
            f"{self.movie.categories.all()[0].name}",
            'test category'
        )
        self.assertEqual(
            f"{self.movie.countries.all()[0].name}",
            'test country'
        )
        self.assertEqual(
            f"{self.movie.directors.all()[0].name}",
            'test director'
        )
        self.assertEqual(
            f"{self.movie.casts.all()[0].name}",
            'test cast'
        )

    def test_create_country(self):
        self.country = Country.objects.create(
            name='test_country'
        )
        self.assertEqual(self.country.name, 'test_country')
        self.assertEqual(Country.objects.all()[1].name, self.country.name)

    def test_create_category(self):
        self.category = Category.objects.create(
            name='test_category'
        )
        self.assertEqual(self.category.name, 'test_category')
        self.assertEqual(Category.objects.all()[1].name, self.category.name)

    def test_movie_search_list_view(self):
        response = self.client.get(
            reverse('search_results'), {'q': self.movie.title}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'{self.movie.title}')
        self.assertTemplateUsed(
            response, 'movies/search_results.html'
        )

    def test_movie_detail_view(self):
        response = self.client.get(self.movie.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'{self.movie.title}')
        self.assertTemplateUsed(
            response, 'movies/movie_detail.html')

    def test_false_movie_detail_view(self):
        response = self.client.get(self.movie.get_absolute_url() + 'test')
        self.assertEqual(response.status_code, 404)

    def test_add_movie_to_watchlist(self):
        watchlist = Watchlist.objects.create(
            user=self.user,
            movie=self.movie,
            saved_date=datetime.now()
        )
        watchlist.save()
        self.assertEqual(watchlist.user.email, 'test@test.com')
        self.assertEqual(watchlist.movie.title, 'The matrix')
        self.assertFalse(watchlist.seen)

    def test_update_movie_to_viewed(self):
        pass

    def test_rating_return_json(self):
        response = self.client.get(f'/movies/rating/{self.movie.id}')
        self.assertEqual(response.status_code, 200)

    def test_save_movie_to_watchlist_without_logging(self):
        response = self.client.get(reverse('save'))
        self.assertEqual(response.status_code, 302)

    def test_save_movie_to_watchlist_with_loggin(self):
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        response = self.client.get(f'/movies/save/?movie={self.movie.id}')
        self.assertEqual(response.status_code, 302)
        # self.assertEqual(Watchlist.objects.all()[0].user_id, self.user.id)
