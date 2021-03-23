from django import forms
from django.forms import ModelForm

class InputForm(forms.Form):
    location = forms.CharField()
    Pop = forms.IntegerField()
    url = forms.CharField()
    api = forms.CharField()

class DateInput(forms.DateInput):
    input_type = "date"

class dateform(forms.Form):
    date_field = forms.DateField(widget=DateInput)
