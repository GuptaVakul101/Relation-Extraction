from django.shortcuts import render, redirect
from .forms import *
from .models import Object

def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            relation = form.cleaned_data['relation']
            NumberOfResults = form.cleaned_data['NumberOfResults']
            result = Object.objects.filter(relation=relation)
            result = result.order_by('?')
            result = result[0:NumberOfResults]
            return render(request, 'home/index.html', {'form' : form, 'result': result})
    else:
        form = SearchForm()
        all_relations = Object.objects.values_list('relation', flat=True)
        all_relations = all_relations.distinct()
        return render(request, 'home/index.html', {'form' : form, 'all_relations': all_relations})

def fill_data(request):
    if request.method == "POST":
        form = FillDataForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES.get('data_file', False):
                data_file = request.FILES['data_file']
                count = 0
                for row in data_file:
                    line = row.split(b'\t')
                    newObject = Object()
                    newObject.object_1 = line[0].decode('utf-8')
                    newObject.object_1_type = line[1].decode('utf-8')
                    newObject.object_2 = line[2].decode('utf-8')
                    newObject.object_2_type = line[3].decode('utf-8')
                    newObject.relation = line[4].decode('utf-8').replace('\n', '').replace('\r', '')
                    newObject.save()
                    count += 1
                    if count >= 100:
                        break
        return redirect('/home/')
    else:
        pass
