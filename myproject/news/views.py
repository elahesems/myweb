from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from main.models import Main
from news.models import News
from django.core.files.storage import FileSystemStorage

def news_detail(request,word):
    site = Main.objects.get(pk=2)

    news= News.objects.filter(name=word)
    context={'news':news, 'site':site}
    return render(request, 'news_detail.html', context)

def news_list(request):

    news = News.objects.all()

    context = {'news':news}

    return render(request, 'back/news_list.html',context)




def news_add(request):
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')


        if newstitle == "" or newstxtshort == "" or newstxt =="" or newscat == "":
            error= "All Fields Requirded"
            return render(request,'back/error.html' ,{'error':error})

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date="2020", pic="url", writer="-", catname=newscat, catid=0, show=0)
        b.save()
        return redirect('news_list')
    return render(request, 'back/news_add.html')