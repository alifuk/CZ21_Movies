from django.forms import (
  CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea, SelectDateWidget
)
import re
from django.forms import ModelForm
from viewer.models import Genre, Movie, Building

def capitalized_validator(value):
  if value[0].islower():
    raise ValidationError('Value must be capitalized.')
class PastMonthField(DateField):

  def validate(self, value):
    super().validate(value)
    if value >= date.today():
      raise ValidationError('Only past dates allowed here.')

  def clean(self, value):
    result = super().clean(value)
    return date(year=result.year, month=result.month, day=1)


class MovieForm(ModelForm):

  class Meta:
    model = Movie
    fields = '__all__'

  #title = CharField(validators=[capitalized_validator])
  #rating = IntegerField(min_value=1, max_value=10)
  #released = PastMonthField()

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

class GenreForm(ModelForm):
  class Meta:
    model = Genre
    fields = '__all__'


class SearchForm(Form):
  search_field = CharField(max_length=128)


from django.contrib.auth.forms import (
  AuthenticationForm, PasswordChangeForm, UserCreationForm
)
class SignUpForm(UserCreationForm):

  class Meta(UserCreationForm.Meta):
    fields = ['username', 'first_name', 'last_name']

  def save(self, commit=True):
    self.instance.is_active = True
    return super().save(commit)




class BuildingForm(ModelForm):

  class Meta:
    model = Building
    fields = '__all__'