from django.shortcuts import render, redirect
from .forms import *
from .models import Object
import random

def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            relation = form.cleaned_data['relation']
            NumberOfResults = form.cleaned_data['NumberOfResults']
            result_relation = []
            with open("./../heirarchy_mapping/dloc_heirarchy.csv", "r") as f:
                for line in f:
                    if relation == line.split(',')[0]:
                        for item in line.split(',')[1:]:
                            print(item)
                            result_relation.append(item)
            with open("./../heirarchy_mapping/dper_heirarchy.csv", "r") as f:
                for line in f:
                    if relation == line.split(',')[0]:
                        for item in line.split(',')[1:]:
                            print(item)
                            result_relation.append(item)
            with open("./../heirarchy_mapping/dorg_heirarchy.csv", "r") as f:
                for line in f:
                    if relation == line.split(',')[0]:
                        for item in line.split(',')[1:]:
                            print(item)
                            result_relation.append(item)
            with open("./../heirarchy_mapping/wloc_heirarchy.csv", "r") as f:
                for line in f:
                    if relation == line.split(',')[0]:
                        for item in line.split(',')[1:]:
                            print(item)
                            result_relation.append(item)
            with open("./../heirarchy_mapping/wper_heirarchy.csv", "r") as f:
                for line in f:
                    if relation == line.split(',')[0]:
                        for item in line.split(',')[1:]:
                            print(item)
                            result_relation.append(item)
            with open("./../heirarchy_mapping/worg_heirarchy.csv", "r") as f:
                for line in f:
                    if relation == line.split(',')[0]:
                        for item in line.split(',')[1:]:
                            print(item)
                            result_relation.append(item)
            result = Object.objects.filter(relation__in=result_relation)
            result = result.distinct()
            result = result[0:NumberOfResults]
            return render(request, 'home/index.html', {'form' : form, 'result': result})
    else:
        form = SearchForm()
        all_relations = list(Object.objects.values_list('relation', flat=True))
        with open("./../heirarchy_mapping/dloc_heirarchy.csv", "r") as f:
            for line in f:
                all_relations.append(line.split(',')[0])
        with open("./../heirarchy_mapping/dper_heirarchy.csv", "r") as f:
            for line in f:
                all_relations.append(line.split(',')[0])
        with open("./../heirarchy_mapping/dorg_heirarchy.csv", "r") as f:
            for line in f:
                all_relations.append(line.split(',')[0])
        with open("./../heirarchy_mapping/wloc_heirarchy.csv", "r") as f:
            for line in f:
                all_relations.append(line.split(',')[0])
        with open("./../heirarchy_mapping/wper_heirarchy.csv", "r") as f:
            for line in f:
                all_relations.append(line.split(',')[0])
        with open("./../heirarchy_mapping/worg_heirarchy.csv", "r") as f:
            for line in f:
                all_relations.append(line.split(',')[0])
        all_relations = list(set(all_relations))
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
