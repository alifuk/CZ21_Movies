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

from viewer.models import Genre, Movie, Actor, Building, Comment
from viewer.views import mypage, hello, search, MoviesView, MovieCreateView, MovieUpdateView, MovieDeleteView, tags_example
from viewer.views import SubmittablePasswordChangeView, SignUpView, GenresView, GenreCreateView, GenreUpdateView, GenreDeleteView
from viewer.views import BuildingView, BuildingCreateView, BuildingUpdateView, BuildingDeleteView, CommentCreateView
from viewer.views import api_moviesgetall, list_movies
from django.contrib.auth import views

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Building)
admin.site.register(Comment)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/', mypage, name='mypage'),

    path('hello/<s0>', hello),
    path('tags_example', tags_example),
    # path('', views.movies), #Function based view
    path('', MoviesView.as_view(), name='index'),  # Class based view
    path('movie/create', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>', MovieDeleteView.as_view(), name='movie_delete'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password_change/', SubmittablePasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),


    path('genres', GenresView.as_view(), name='genres'),  # Class based view
    path('genre/create', GenreCreateView.as_view(), name='genre_create'),
    path('genre/update/<pk>', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<pk>', GenreDeleteView.as_view(), name='genre_delete'),
    path('search', search, name='search'),  # Class based view


    path('building', BuildingView.as_view(), name='building'),
    path('building/create', BuildingCreateView.as_view(), name='building_add'),
    path('building/update/<pk>', BuildingUpdateView.as_view(), name='building_update'),
    path('building/delete/<pk>', BuildingDeleteView.as_view(), name='building_delete'),

    path('comment/create/<pk>', CommentCreateView.as_view(), name='comment_add'),


    path('api/movies/get_all', api_moviesgetall, name='api_moviesgetall'),



    path('list_movies', list_movies, name='list_movies'),
]
