from django.test import TestCase
from rest_framework import status
from .models import User


class UserModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'some@email.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 25,
        }
        cls.user = User.objects.create(**cls.user_data)

    def test_user_instance(self):
        self.assertIsInstance(self.user, User)

    def test_user_attributes(self):
        self.assertEqual(self.user.username, self.user_data['username'])
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertEqual(self.user.first_name, self.user_data['first_name'])
        self.assertEqual(self.user.last_name, self.user_data['last_name'])
        self.assertEqual(self.user.age, self.user_data['age'])


class UserModelViewSetTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # cls.client = APIClient()
        cls.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'some@email.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 25,
        }

    def test_create_user(self):
        response = self.client.post('/users/api/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(username=self.user_data['username'])
        self.assertEqual(user.first_name, self.user_data['first_name'])
        self.assertEqual(user.last_name, self.user_data['last_name'])
        self.assertEqual(user.age, self.user_data['age'])

    def test_get_user(self):
        user = User.objects.create(**self.user_data)
        response = self.client.get(f'/users/api/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user_data['username'])
        self.assertEqual(response.data['first_name'], self.user_data['first_name'])
        self.assertEqual(response.data['last_name'], self.user_data['last_name'])
        self.assertEqual(response.data['age'], self.user_data['age'])

    def test_delete_user(self):
        user = User.objects.create(**self.user_data)
        response = self.client.delete(f'/users/api/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=user.id).exists())
