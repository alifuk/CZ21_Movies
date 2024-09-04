from django.shortcuts import render
from viewer.models import Movie
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView
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


class MovieCreateView(CreateView):

  template_name = 'form.html'
  form_class = MovieForm
  success_url = reverse_lazy('movie_create')

  def form_invalid(self, form):
    LOGGER.warning(f'User provided invalid data. {form.errors}')
    return super().form_invalid(form)

    
class MovieUpdateView(UpdateView):

  template_name = 'form.html'
  model = Movie
  form_class = MovieForm
  success_url = reverse_lazy('index')

  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data while updating a movie.')
    return super().form_invalid(form)


class MovieDeleteView(DeleteView):
  template_name = 'movie_confirm_delete.html'
  model = Movie
  success_url = reverse_lazy('index')