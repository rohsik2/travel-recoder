from django import forms
from .models import *
from django.forms import modelformset_factory
from django.forms import formset_factory

class TravelForm(forms.ModelForm):
    image = forms.FileField(required=True)
    start_date = forms.DateField(
        help_text="Departure Date ex) 2020-12-31")
    end_date = forms.DateField(
        help_text="Arrival Date ex) 2020-12-31")

    class Meta:
        model = Travel
        fields = ('title', 'description')

class LocationForm(forms.ModelForm):
    class Meta:
        model = TravelLocation
        fields = ('day','title','description')

class LocationImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = TravelLocationImage
        fields = ('images',)