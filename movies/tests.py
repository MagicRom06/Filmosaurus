from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from movies.models import Category, Country, Movie, Person, Watchlist

# Create your tests here.


class MoviesTest(TestCase):
    """
    testing movies app
    """
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
        """
        testing new movie creation and data saved
        """
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
        """
        testing country creation and saved data
        """
        self.country = Country.objects.create(
            name='test_country'
        )
        self.assertEqual(self.country.name, 'test_country')
        self.assertEqual(Country.objects.all()[1].name, self.country.name)

    def test_create_category(self):
        """
        testing categories creation and data saved
        """
        self.category = Category.objects.create(
            name='test_category'
        )
        self.assertEqual(self.category.name, 'test_category')
        self.assertEqual(Category.objects.all()[1].name, self.category.name)

    def test_str_movie_is_equal_to_title(self):
        """
        testing __str__ for movie model
        """
        movie = Movie.objects.get(title=self.movie.title)
        self.assertEqual(str(movie), movie.title)

    def test_str_country_is_equal_to_title(self):
        """
        testing __str__ for country model
        """
        country = Country.objects.get(name='test country')
        self.assertEqual(str(country), country.name)

    def test_str_category_is_equal_to_title(self):
        """
        testing __str__ for category model
        """
        category = Category.objects.get(name='test category')
        self.assertEqual(str(category), category.name)

    def test_str_person_is_equal_to_title(self):
        """
        testing __str__ for person model
        """
        person = Person.objects.get(name='test director')
        self.assertEqual(str(person), person.name)

    def test_movie_search_list_view(self):
        """
        testing the movie search from home
        """
        response = self.client.get(
            reverse('search_results'), {'q': self.movie.title}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'{self.movie.title}')
        self.assertTemplateUsed(
            response, 'movies/search_results.html'
        )

    def test_movie_detail_view(self):
        """
        testing the movie detail view
        """
        response = self.client.get(self.movie.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'{self.movie.title}')
        self.assertTemplateUsed(
            response, 'movies/movie_detail.html')

    def test_false_movie_detail_view(self):
        """
        testing movie detail rendering with false movie
        """
        response = self.client.get(self.movie.get_absolute_url() + 'test')
        self.assertEqual(response.status_code, 404)

    def test_add_movie_to_watchlist(self):
        """
        testing to save a movie in watchlist
        """
        watchlist = Watchlist.objects.create(
            user=self.user,
            movie=self.movie,
            saved_date=datetime.now()
        )
        watchlist.save()
        self.assertEqual(watchlist.user.email, 'test@test.com')
        self.assertEqual(watchlist.movie.title, 'The matrix')
        self.assertFalse(watchlist.seen)

    def test_rating_return_json(self):
        """
        testing status code for rating movie
        while logged
        """
        response = self.client.get(f'/movies/rating/{self.movie.id}')
        self.assertEqual(response.status_code, 200)

    def test_save_movie_to_watchlist_without_logging(self):
        """
        testing status code for rating movie
        while not logged
        """
        response = self.client.get(reverse('save'))
        self.assertEqual(response.status_code, 302)

    def test_advanced_search_view(self):
        """
        testing advanced search view
        """
        response = self.client.get(reverse('advanced_search'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Advanced Search')
        self.assertTemplateUsed(
            response, 'movies/advanced_search.html'
        )

    def test_advanced_search_for_director(self):
        """
        testing status code when make director search
        """
        response = self.client.get(
            '/movies/advanced/search/results?by_director=test'
        )
        self.assertEqual(response.status_code, 200)

    def test_advanced_search_for_actor(self):
        """
        testing status code when make actor search
        """
        response = self.client.get(
            '/movies/advanced/search/results?by_casting=test'
        )
        self.assertEqual(response.status_code, 200)

    def test_save_movie_to_watchlist_with_loggin(self):
        """
        testing add in watchlist while logged
        """
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        response = self.client.get(f'/movies/save/?movie={self.movie.id}')
        self.assertEqual(response.status_code, 302)
