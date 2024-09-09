"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from viewer.models import Genre, Movie
from viewer.views import hello, search, MoviesView, MovieCreateView, MovieUpdateView, MovieDeleteView, tags_example
from viewer.views import GenresView, GenreCreateView, GenreUpdateView, GenreDeleteView

admin.site.register(Genre)
admin.site.register(Movie)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<s0>', hello),
    path('tags_example', tags_example),
    #path('', views.movies), #Function based view
    path('', MoviesView.as_view(), name='index'), #Class based view
    path('movie/create', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>', MovieDeleteView.as_view(), name='movie_delete'),    
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('genres', GenresView.as_view(), name='genres'), #Class based view
    path('genre/create', GenreCreateView.as_view(), name='genre_create'),
    path('genre/update/<pk>', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<pk>', GenreDeleteView.as_view(), name='genre_delete'),
    path('search', search, name='search'),  # Class based view

]