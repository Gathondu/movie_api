from data import movies
from django.http import JsonResponse

def index(request):
    return JsonResponse(movies, safe=False)

def get_movie(request, movie_id):
    for movie in movies:
        if movie['id'] == movie_id:
            return JsonResponse(movie)
    return JsonResponse({'error': 'No movie with that id'}, status=404)