from django.shortcuts import render


# Create your views here.

def index(request):
    data = {'caption': 'Первая страница'}
    return render(request, 'main/index.html', data)

def new(request):
    data2 = {'caption': 'Вторая страница'}
    return render(request, 'main/new.html', data2)

