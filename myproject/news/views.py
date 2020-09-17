from django.shortcuts import render, get_object_or_404, redirect

from cat.models import Cat
from main.models import Main
from news.forms import NewsForm
from news.models import News
from django.core.files.storage import FileSystemStorage
import datetime


#from main.dateconverter import
# Create your views here.
from subcat.models import SubCat


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
    form = NewsForm()
    now = datetime.datetime.now()
    print(now)
    year = now.year
    month = now.month
    day = now.day
    print(day)

    if len(str(day)) == 1 :
        day = "0" + str(day)
    if len(str(month)) == 1 :
        month = "0" + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(now.hour) + ":" + str(now.minute)

    cat = SubCat.objects.all()


    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')


        if newstitle == "" or newstxtshort == "" or newstxt =="" or newscat == "":
            error= "All Fields Requirded"
            return render(request,'back/news_add.html' ,{'error':error,'now':now,'form':form})


        try:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000 :

                    newsname = SubCat.objects.get(pk=newsid).name

                    b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=now, picname=filename, picurl=url, writer="-", catname=newsname, catid=newsid, show=0, time=time)
                    b.save()
                    return redirect('news_list')

                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)

                    error = "Your File Is Bigger Than 5 MB"
                    return render(request, 'back/error.html', {'error': error})


            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your File Not Supported"
                return render(request, 'back/error.html', {'error': error})

        except:
            error = "Please Input Your Image"
            return render(request, 'back/error.html', {'error': error})

    context = {'now':now,'form':form,'cat':cat}
    return render(request, 'back/news_add.html',context)


def news_delete(request,pk):
    try:
        b = News.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(b.picname)
        b.delete()
    except:
        error = "Somthing Wrong"
        return render(request,'back/error.html',{'error':error})
    return redirect('news_list')

def news_edit(request,pk):

    if len(News.objects.filter(pk=pk)) == 0 :
        error = "News Not Found"
        return render(request, 'back/error.html' , {'error':error})


    news = News.objects.get(pk=pk)
    cat = SubCat.objects.all()
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')


        if newstitle == "" or newstxtshort == "" or newstxt =="" or newscat == "":
            error= "All Fields Requirded"
            return render(request,'back/news_add.html' ,{'error':error})


        try:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000 :

                    newsname = SubCat.objects.get(pk=newsid).name

                    b = News.objects.get(pk=pk)
                    fss = FileSystemStorage()
                    fss.delete(b.picname)

                    b.name = newstitle
                    b.short_txt = newstxtshort
                    b.body_txt = newstxt
                    b.picname = filename
                    b.picurl = url
                    b.catname = newsname
                    b.catid = newsid
                    b.save()
                    return redirect('news_list')

                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)

                    error = "Your File Is Bigger Than 5 MB"
                    return render(request, 'back/error.html', {'error': error})


            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your File Not Supported"
                return render(request, 'back/error.html', {'error': error})

        except:
            newsname = SubCat.objects.get(pk=newsid).name

            b = News.objects.get(pk=pk)

            b.name = newstitle
            b.short_txt = newstxtshort
            b.body_txt = newstxt
            b.catname = newsname
            b.catid = newsid
            b.save()
            return redirect('news_list')



    context = {'pk':pk,'news':news,'cat':cat}

    return render(request, 'back/news_edit.html', context)

