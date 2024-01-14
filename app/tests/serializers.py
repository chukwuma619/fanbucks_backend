# tests.py in your app directory

from django.test import TestCase
from app.serializers import UserSerializer, CreateUserSerializer


class UserSerializerTest(TestCase):
    def test_user_serializer(self):
        user_data = {'username': 'testuser@example.com',
                     'password': 'testpassword',
                     'first_name': 'testuser',
                     'last_name': 'something'}
        serializer = CreateUserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()

        # Test UserSerializer
        user_serializer = UserSerializer(user)
        self.assertTrue(user_serializer.data)

        # Add more tests as needed
