from django.shortcuts import render
from .models import Newspost

# Create your views here.

def home(request):
    news = Newspost.objects.all()
    return render(request, 'news/news.html', {'news': news})
