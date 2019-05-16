from django.shortcuts import render
from movies.models import *

# Create your views here.
def movies(request):
    movies = Movie.objects.all().order_by('year')
    return render(request, 'movies.html', {
        'movies': movies
    })

def movie_details(request,movie_id):
    movie = Movie.objects.get(pk=movie_id)
    starring = movie.starring.all()
    roles = PersonMovie.objects.filter(movie=movie_id)
    actors = zip(starring, roles)
    return render(request, 'movie_details.html', {
        'movie': movie,
        'actors': actors,
    })