import json

from django.test import SimpleTestCase
from django.utils.encoding import force_text

from data import movies
from movies.utils import binarySearch, linearSearch


class MovieTestCase(SimpleTestCase):
    def setUp(self):
        self.movies = movies

    def test_we_get_all_movies(self):
        response = self.client.get('/api/v1/movies/')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['count'], len(self.movies))

    def test_we_get_specific_movie(self):
        response = self.client.get('/api/v1/movies/1')
        movie = binarySearch(self.movies, 0, len(self.movies) - 1, 1)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(force_text(response.content), movie)

    def test_unavailable_movie_id_fails(self):
        response = self.client.get('/api/v1/movies/2001')
        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(force_text(response.content), {'error': 'No movie with that id'})

    def test_search_for_name(self):
        response = self.client.get('/api/v1/movies/search?name=ton')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        results = linearSearch(self.movies, 'name', 'ton')
        self.assertEqual(data['count'], len(results))
        self.assertEqual(data['movies'][0], results[0])

    def test_search_for_genre(self):
        response = self.client.get('/api/v1/movies/search?genre=drama')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        results = linearSearch(self.movies, 'genre', 'drama')
        self.assertEqual(data['count'], len(results))
        self.assertEqual(data['movies'][0], results[0])

    def test_search_using_wrong_key(self):
        response = self.client.get('/api/v1/movies/search?showing_time=10:18')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(force_text(response.content), {'error': 'You can only search name or genre of a movie.'})