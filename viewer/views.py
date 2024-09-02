from django.shortcuts import render
from viewer.models import Movie
from django.views.generic import FormView, ListView
from logging import getLogger
from viewer.forms import MovieForm
from django.urls import reverse_lazy

def hello(request, s0):
  s1 = request.GET.get('s1', '')
  return render(
    request, template_name='hello.html',
    context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
  )


def movies(request):
  return render(
    request, template_name='movies.html',
    context={'movies': Movie.objects.all()}
  )
  
class MoviesView(ListView):
  template_name = 'movies.html'
  model = Movie
  
LOGGER = getLogger()

class MovieCreateView(FormView):

  template_name = 'form.html'
  form_class = MovieForm
  success_url = reverse_lazy('movie_create')

  def form_valid(self, form):
    result = super().form_valid(form)
    cleaned_data = form.cleaned_data
    Movie.objects.create(
      title=cleaned_data['title'],
      genre=cleaned_data['genre'],
      rating=cleaned_data['rating'],
      released=cleaned_data['released'],
        description=cleaned_data['description']
    )
    return result

  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data.')
    return super().form_invalid(form)