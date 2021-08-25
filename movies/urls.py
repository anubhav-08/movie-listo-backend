from django.urls import path
from .views import store, MoviesList


urlpatterns=[
    path('list/movies', MoviesList.as_view()),
    path('internal/store/movies', store),
]
