from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from news.models import News


def news_detail(request,pk):

    news= News.objects.filter(pk=pk)
    context={'news':news}
    return render(request, 'news_detail.html', context)
