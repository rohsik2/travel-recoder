from django import forms
from .models import *


class TravelForm(forms.ModelForm):
    image = forms.FileField(required=True)
    start_date = forms.DateField(
        help_text="Enter a date start travel 12/31/2020")
    end_date = forms.DateField(
        help_text="Enter a date end travel 12/31/2020")

    class Meta:
        model = Travel
        fields = ('title', 'description')

