from data import movies
from django.http import JsonResponse

def index(request):
    return JsonResponse(movies, safe=False)
