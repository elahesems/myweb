from django.shortcuts import render, get_object_or_404, redirect

from news.models import News
from .models import Main
# Create your views here.from news.models import News


def home(request):

    site = Main.objects.get (pk=2)
    news= News.objects.all()
    context={'site': site, 'news':news}
    return render(request, 'home.html', context)


def about(request):


    site = Main.objects.get (pk=2)

    context={'site': site}

    return render(request, 'about.html', context)