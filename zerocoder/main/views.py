from django.shortcuts import render


# Create your views here.

def index(request):
    data = {'caption': 'Графики и диаграммы'}
    return render(request, 'main/index.html', data)

def new(request):
    data2 = {'caption': 'Виды графиков и диаграмм'}
    return render(request, 'main/new.html', data2)

