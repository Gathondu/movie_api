import json

from data import movies
from django.test import TestCase
from django.utils.encoding import force_text

class MovieTestCase(TestCase):
    def setUp(self):
        self.movies = movies

    def test_we_get_all_movies(self):
        response = self.client.get('/movies/')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1000)


    def test_we_get_specific_movie(self):
        response = self.client.get('/movie/1')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(force_text(response.content), self.movies[0])