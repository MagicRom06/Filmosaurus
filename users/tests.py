from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.


class CustomUserTests(TestCase):
    """
    testing new user creation
    """
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test_user',
            email='test@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """
        testing new super user creation
        """
        User = get_user_model()
        user = User.objects.create_superuser(
            username='super_test_user',
            email='test@email.com',
            password='super_testpass123'
        )
        self.assertEqual(user.username, 'super_test_user')
        self.assertEqual(user.email, 'test@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
