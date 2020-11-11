from rest_framework import serializers
from movielist.models import Movie, Person
from showtimes.models import Cinema, Screening


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie'
    )

    class Meta:
        model = Cinema
        fields = ['id', 'movies', 'city', 'name']

class ScreeningSerializer(serializers.ModelSerializer):
    cinema = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Cinema.objects.all())
    movie = serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all())

    class Meta:
        model = Screening
        fields = ['id', 'cinema', 'movie']
