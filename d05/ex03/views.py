from django.shortcuts import render
from django.http import HttpResponse
from django.db.utils import IntegrityError, Error

from .models import Movie

# Create your views here.

def populate(request):
    try:
        Movie.objects.create(title='The Phantom Menace', director='George Lucas', producer='Rick McCallum', release_date='1999-05-19')
        Movie.objects.create(title='Attack of clones', director='George Lucas', producer='Rick McCallum', release_date='2002-05-16')
        
        # movie = Movie(title='Attack of clones', director='George Lucas', producer='Rick McCallum', release_date='2002-05-16')
        # movie.save()
        content = 'OK'
    except Error as err:
        content = str(err)
    return HttpResponse(f'<p>{content}</p>')

def display(request):
    movies = Movie.objects.all()
    movie = movies[0]
    # print(movie.title) #, movie.crawling_text)
    return render(request, 'ex03/display.html', {'movies': movies})

def remove(request):
    if request.POST:
        id = int(request.POST['episode_nb'])
        Movie.objects.get(episode_nb=id).delete()
    movies = Movie.objects.all().values('episode_nb', 'title')
    print(movies)
    context = {'movies': movies}
    return render(request, 'ex03/remove.html', context)

def update(request):
    if request.POST:
        id = int(request.POST['episode_nb'])
        value = request.POST['crawling_text']
        print(id, value)
        movie_to_update = Movie.objects.get(episode_nb=id)
        # movie_to_update.update(crawling_text=value)
        movie_to_update.opening_crawl = value
        # print(movie_to_update)
        movie_to_update.save()
    movies = Movie.objects.all().values('episode_nb', 'title')
    # print(movies)
    context = {'movies': movies}
    return render(request, 'ex03/update.html', context)
