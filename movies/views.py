from .models import Movie
from .serializers import MovieSerializer
from rest_framework import mixins, generics
from rest_framework.response import Response
from .utils import storeMovies

class MoviesList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

def store(request):
    storeMovies()
    return Response({"message" : "Movies stored successfully"})