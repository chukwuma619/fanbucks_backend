from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

class UserViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser@example.com',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

    def test_user_get(self):
        response = self.client.get('/api/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        update_data = {'first_name': 'UpdatedFirstName', 'last_name': 'UpdatedLastName'}
        response = self.client.put('/api/user/', data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
