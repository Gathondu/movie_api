from django.urls import path
import movies.views as views

urlpatterns = [
    path('', views.index),
    path('<int:movie_id>', views.get_movie),
    path('search', views.search),
]