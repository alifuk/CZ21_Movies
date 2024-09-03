from django.forms import (
  CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea, SelectDateWidget
)
import re
from django.forms import ModelForm
from viewer.models import Genre, Movie
from viewer.validators import capitalized_validator, PastMonthField

class MovieForm(ModelForm):

  class Meta:
    model = Movie
    fields = '__all__'

  title = CharField(validators=[capitalized_validator])
  rating = IntegerField(min_value=1, max_value=10)
  released = PastMonthField()

  def clean_description(self):
    # Každá věta bude začínat velkým písmenem
    initial = self.cleaned_data['description']
    sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
    return '. '.join(sentence.capitalize() for sentence in sentences)

  def clean(self):
    result = super().clean()
    if result['genre'].name == 'commedy' and result['rating'] > 5:
      raise ValidationError(
        "Commedies aren't so good to be rated over 5."
      )
    return result