from data import movies
from django.http import JsonResponse
from movies.utils import binarySearch, linearSearch

def index(request):
    return JsonResponse(movies, safe=False)

def get_movie(request, movie_id):
    movie = binarySearch(movies, 0, len(movies)-1, movie_id)
    if movie:
        return JsonResponse(movie)
    return JsonResponse({'error': 'No movie with that id'}, status=404)

def search(request):
    results = []
    for key in request.GET.keys():
        query = request.GET.get(key, None)
        if key in ('name', 'genre') and query:
            results.extend(linearSearch(movies, key, query))
        else:
            return JsonResponse({'error': 'You can only search name and genre of a movie.'}, status=400)
    return JsonResponse(results, safe=False)
