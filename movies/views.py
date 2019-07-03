from django.http import JsonResponse

def index(request):

    return JsonResponse({'set': 'bar'})
