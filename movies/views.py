from data import movies
from django.http import JsonResponse
from movies.utils import binarySearch

def index(request):
    return JsonResponse(movies, safe=False)

def get_movie(request, movie_id):
    movie = binarySearch(movies, 0, len(movies)-1, movie_id)
    if movie:
        return JsonResponse(movie)
    return JsonResponse({'error': 'No movie with that id'}, status=404)