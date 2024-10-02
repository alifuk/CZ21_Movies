from django.db.models import (
  DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
  Model, TextField, ManyToManyField
)


class Genre(Model):
  name = CharField(max_length=128)



class Movie(Model):
  title = CharField(max_length=128)
  genre = ForeignKey(Genre, on_delete=DO_NOTHING)
  rating = IntegerField()
  released = DateField()
  description = TextField(default="no description")
  created = DateTimeField(auto_now_add=True)

class Actor(Model):
  first_name = CharField(max_length=128)
  last_name = CharField(max_length=128)
  movies = ManyToManyField(Movie)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

from django.contrib.auth import get_user_model
User = get_user_model()

class Building(Model):
  company = CharField(max_length=128)
  floors = IntegerField()
  user = ForeignKey(User, on_delete=DO_NOTHING, default=1)


class Comment(Model):
  movie = ForeignKey(Movie, on_delete=DO_NOTHING, default=1)
  text = CharField(max_length=128)

  def __str__(self):
    return f"Komentář: {self.text} k filmu {self.movie.title}"