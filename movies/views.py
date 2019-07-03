from data import movies
from django.http import JsonResponse
from movies.utils import binarySearch, linearSearch

def index(request):
    return JsonResponse({ 'count': len(movies), 'movies': movies})

def get_movie(request, movie_id):
    movie = binarySearch(movies, 0, len(movies)-1, movie_id)
    if movie:
        return JsonResponse(movie)
    return JsonResponse({'error': 'No movie with that id'}, status=404)

def search(request):
    results = []
    keys = [key.lower() for key in request.GET.keys() if key.lower() in ('name', 'genre')]
    if len(keys) == 1:
        query = request.GET.get(keys[0], None)
        results.extend(linearSearch(movies, keys[0], query))
    else:
        return JsonResponse({'error': 'You can only search name or genre of a movie.'}, status=400)
    return JsonResponse({'count': len(results), 'movies': results})
