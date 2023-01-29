from django.forms import forms
from django.forms import ModelForm
from .models import Galary


class GalaryForm(ModelForm):
    class Meta:
        model = Galary

        fields = ['name', 'description','image']

 
   