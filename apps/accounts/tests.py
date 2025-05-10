from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):

    def test_create_user_with_valid_email_successful(self):
        email = 'test@example.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='Testpass123')

    def test_create_superuser(self):
        email = 'superuser@example.com'
        password = 'Superpass123'
        user = get_user_model().objects.create_superuser(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)