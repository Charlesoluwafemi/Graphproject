# api/tests/test_views.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class NamespaceTests(APITestCase):
    def test_create_namespace(self):
        url = reverse('create_database')
        data = {'name': 'test_namespace'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
