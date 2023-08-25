from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class TestListCreateTodos(APITestCase):

    def authenticate(self):
        self.client.post(reverse("register"),{'username':'username', 'email':'email@email.com','password':'password'})
        response = self.client.post(reverse("login"),{'email':'email@email.com','password':'password'})
        # data=response.data["token"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token'] }  ")

    def test_creates_todo_without_auth(self):
        sample_todo = {"title": "title", "desc": "description"}
        response = self.client.post(reverse('todos'), sample_todo)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_creates_todo(self):
        self.authenticate()
        sample_todo = {"title": "title", "desc": "description"}
        response = self.client.post(reverse('todos'), sample_todo)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



