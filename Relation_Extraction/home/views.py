from django.shortcuts import render
from .forms import SearchForm
from .models import Object

def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            newObject = Object()
            newObject.relation = form.cleaned_data['relation']
            result = Object.objects.filter(relation=newObject.relation)
            return render(request, 'home/index.html', {'form' : form, 'result': result})
    else:
        form = SearchForm()
        return render(request, 'home/index.html', {'form' : form})
