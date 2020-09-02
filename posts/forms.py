from django import forms
from .models import *


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