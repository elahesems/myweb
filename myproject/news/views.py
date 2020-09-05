from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from main.models import Main
from news.models import News


def news_detail(request,word):
    site = Main.objects.get(pk=2)

    news= News.objects.filter(name=word)
    context={'news':news, 'site':site}
    return render(request, 'news_detail.html', context)

def news_list(request):

    return render(request, 'back/news_list.html')