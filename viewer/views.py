from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from viewer.models import Movie, Genre
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView
from logging import getLogger
from viewer.forms import MovieForm, GenreForm, SearchForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import CreateView

from viewer.forms import (
  SignUpForm
)


def hello(request, s0):
  s1 = request.GET.get('s1', '')
  return render(
    request, template_name='hello.html',
    context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
  )

@login_required
def search(request):
    to_find = request.GET.get("search_field", "")
    return render(
        request, template_name='search.html', context={
            "movies": Movie.objects.filter(title__contains=to_find),
            "genres": Genre.objects.filter(name__contains=to_find),
            "search_form": SearchForm,
        }
    )

def movies(request):
  return render(
    request, template_name='movies.html',
    context={'movies': Movie.objects.all()}
  )

def tags_example(request):
  return render(
    request, template_name='tags_example.html',
    context={'movies': Movie.objects.all(),
              "first_movie": Movie.objects.first(),
              "notebooky": {
                  "Lucie": "Asus",
                  "Karel": "Lenovo",
                },
              "jmeno": "Albert",
              "vek": 77.9800,
              "kids": ["Julie", "Aleš", "Karel"],
              "lineexample": "Radek1\n radek2",
              "pocet_kusu": 6,
              "value": timezone.now()
        }
) 
LOGGER = getLogger()
  
class MoviesView(ListView):
  template_name = 'movies.html'
  model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):

  template_name = 'form.html'
  form_class = MovieForm
  success_url = reverse_lazy('movie_create')

  def form_invalid(self, form):
    LOGGER.warning(f'User provided invalid data. {form.errors}')
    return super().form_invalid(form)

    
class MovieUpdateView(PermissionRequiredMixin, UpdateView):

  template_name = 'form.html'
  model = Movie
  form_class = MovieForm
  success_url = reverse_lazy('index')
  permission_required = 'viewer.change_movie'

  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data while updating a movie.')
    return super().form_invalid(form)


class MovieDeleteView(DeleteView):
  template_name = 'movie_confirm_delete.html'
  model = Movie
  success_url = reverse_lazy('index')

class GenresView(ListView):
  template_name = 'genres.html'
  model = Genre

class GenreCreateView(CreateView):
  template_name = 'genre_form.html'
  form_class = GenreForm
  success_url = reverse_lazy('genres')

  def form_invalid(self, form):
      LOGGER.warning(f'User provided invalid data. {form.errors}')
      return super().form_invalid(form)

class GenreUpdateView(UpdateView):
  template_name = 'genre_form.html'
  model = Genre
  form_class = GenreForm
  success_url = reverse_lazy('genres')

  def form_invalid(self, form):
      LOGGER.warning('User provided invalid data while updating a movie.')
      return super().form_invalid(form)

class GenreDeleteView(DeleteView):
  template_name = 'genre_confirm_delete.html'
  model = Genre
  success_url = reverse_lazy('genres')



class SignUpView(CreateView):
  template_name = 'form.html'
  form_class = SignUpForm
  success_url = reverse_lazy('index')

class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'form.html'