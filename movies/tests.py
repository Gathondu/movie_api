import json

from django.test import TestCase

class MovieTestCase(TestCase):
    def test_we_get_all_movies(self):
        response = self.client.get('/movies/')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1000)