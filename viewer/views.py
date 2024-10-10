from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from viewer.models import Movie, Genre, Building, Comment
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView, TemplateView
from logging import getLogger
from viewer.forms import MovieForm, GenreForm, SearchForm, BuildingForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import CreateView

from viewer.forms import (
  SignUpForm
)
from django.contrib.auth.models import User
def mypage(request):
    return render(
        request,
        "mypage.html",
        context={}
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

@login_required
def add_user_to_group(request):
    from django.contrib.auth.models import Group
    request.user.groups.add(Group.objects.first())
    pass

    return render(
        request, template_name='movies.html',
        context={'movies': Movie.objects.all()}
    )


def movies(request):

  request.user.groups.append()
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


class MovieCreateView(PermissionRequiredMixin, CreateView):

  template_name = 'form.html'
  form_class = MovieForm
  success_url = reverse_lazy('movie_create')
  permission_required = 'viewer.add_movie'

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

class GenresView(LoginRequiredMixin ,ListView):
  template_name = 'genres.html'
  model = Genre

class GenreCreateView(PermissionRequiredMixin,CreateView):
  template_name = 'genre_form.html'
  form_class = GenreForm
  success_url = reverse_lazy('genres')
  permission_required = 'viewer.add_building'

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




class BuildingView(TemplateView):
  template_name = 'building.html'
  extra_context = {'buildings': Building.objects.all()}

class BuildingCreateView(CreateView):
  template_name = 'building_form.html'
  form_class = BuildingForm
  success_url = reverse_lazy('building')

class BuildingUpdateView(UpdateView):
  template_name = 'building_form.html'
  model = Building
  form_class = BuildingForm
  #success_url = reverse_lazy('building')

  def get_success_url(self):
      kategorie_pk = Building.objects.get(pk= self.kwargs['pk']).kategorie.pk
      return reverse_lazy('company', kwargs={'pk': kategorie_pk})

class BuildingDeleteView(DeleteView):
  template_name = 'building_form.html'
  model = Building
  success_url = reverse_lazy('building')

class CommentCreateView(FormView):
    template_name = 'form.html'
    form_class = CommentForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.movie = Movie.objects.get(pk=int(self.kwargs["pk"]))
        new_comment.save()
        return super().form_valid(form)
    pass


def api_moviesgetall(request):
    all_movies = Movie.objects.all()
    json_movies = {}
    for movie in all_movies:
        json_movies[movie.pk] = {
            "title": movie.title
        }
    return JsonResponse(json_movies)

def list_movies(request):
    import requests
    responce = requests.get("http://127.0.0.1:8000/api/movies/get_all")
    filmy = responce.json()
    return render(request, "list_movies.html", context={"movies": filmy})
