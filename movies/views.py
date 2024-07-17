from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieStatsSerializer, MovieListDetailSerializer
from app.permissions import GlobalDefaultPermissions
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()
    # serializer_class = MovieModelSerializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer
    

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions, )
    queryset = Movie.objects.all()
    # serializer_class = MovieModelSerializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer

class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions, )
    queryset = Movie.objects.all()
    def get(self, resquest):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data={
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews, 
            'average_stars': round(average_stars, 1) if average_stars else 0
        }
        serializer = MovieStatsSerializer(data=data) 
        serializer.is_valid(raise_exception=True)

        return response.Response(data=serializer.validated_data,status=status.HTTP_200_OK)
    
    def post(self, resquest):#TODO: método post
        ...