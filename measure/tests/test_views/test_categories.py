import json

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ...models import Category


class CategoriesTestCase(APITestCase):
    def test_empty_db_empty_response(self):
        url = reverse('measure:category-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(json.loads(response.content.decode('utf-8')))

    def test_some_objects_in_db_some_in_response(self):
        Category.objects.create(name='weight')
        Category.objects.create(name='height')

        url = reverse('measure:category-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(
            json.loads(response.content.decode('utf-8')),
            [
                {'name': 'weight'},
                {'name': 'height'},
            ]
        )