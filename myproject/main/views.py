from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
# Create your views here.


def home(request):

    sitename = "MySite | Home"

    context={'sitename': sitename}
    return render(request, 'home.html', context)


def about(request):


    sitename = "MySite | About"

    context={'sitename': sitename}

    return render(request, 'about.html', context)