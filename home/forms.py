from django import forms
class WordForm(forms.Form):
    letters = forms.CharField(max_length=100)