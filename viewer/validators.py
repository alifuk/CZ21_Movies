import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import (
  CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea
)

from viewer.models import Genre
