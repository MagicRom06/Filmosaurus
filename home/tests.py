from home.views import HomePageView
from django.test import TestCase
from django.urls import reverse, resolve

# Create your tests here.


class HomePageTests(TestCase):
    """
    Testing home page
    """

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home/home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Watch and enjoy !')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
