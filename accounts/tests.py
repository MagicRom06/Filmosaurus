from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class AccountsTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_username',
            email="test@test.com",
            password="test1234"
        )

    def test_account_page_view(self):
        """
        testing account page access
        """
        self.client.login(username='test@test.com', password='test1234')
        response = self.client.get(reverse('accounts'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, self.user.email)
        self.assertTemplateUsed(response, 'accounts/accounts.html')

    def test_reset_password_page(self):
        response = self.client.get(reverse('account_reset_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/password_reset.html')

    def test_signup_template(self):
        self.response = self.client.get(reverse('account_signup'))
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Signup')

    def test_signup_form(self):
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(
            get_user_model().objects.all()[0].email, self.user.email)


class EmailTest(TestCase):

    def test_send_email(self):
        mail.send_mail(
            'test subject', 'test message',
            'notification-filmosaurus@monaco.mc', ['test@example.com'],
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'test subject')
        self.assertEqual(mail.outbox[0].body, 'test message')
