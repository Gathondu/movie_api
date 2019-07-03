import json

from data import movies
from django.test import SimpleTestCase
from django.utils.encoding import force_text

class MovieTestCase(SimpleTestCase):
    def setUp(self):
        self.movies = movies

    def test_we_get_all_movies(self):
        response = self.client.get('/api/v1/movies/')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1000)

    def test_we_get_specific_movie(self):
        response = self.client.get('/api/v1/movies/1')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(force_text(response.content), self.movies[0])

    def test_unavailable_movie_id_fails(self):
        response = self.client.get('/api/v1/movies/2001')
        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(force_text(response.content), {'error': 'No movie with that id'})

    def test_search_for_name(self):
        response = self.client.get('/api/v1/movies?name=ton')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        # searching ton should get us 8 results of movies with the substring ton
        self.assertEqual(len(data), 8)
        # Since we are using a linear search, the 1st item matching this criterion
        # is at index 8
        self.assertJSONEqual(force_text(data[0]), self.movies[8])

    def test_search_for_genre(self):
        pass