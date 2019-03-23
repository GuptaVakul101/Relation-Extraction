from django import forms

class SearchForm(forms.Form):
    relation = forms.CharField(label='relation', max_length=500)

class FillDataForm(forms.Form):
    data_file = forms.FileField(label='data_file')
