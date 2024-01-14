# tests.py in your app directory

from django.test import TestCase
from app.models import User
class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser@example.com', password='testpassword')
        self.assertIsInstance(user, User)
        self.assertEqual(User.objects.count(), 1)
