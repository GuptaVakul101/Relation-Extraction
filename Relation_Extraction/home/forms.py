from django import forms

class SearchForm(forms.Form):
    relation = forms.CharField(label='relation', max_length=100)
