from django.shortcuts import render, get_object_or_404, redirect

from cat.models import Cat
from main.models import Main
# Create your views here.


def cat_list(request):
    cat = Cat.objects.all()

    context = {'cat':cat}
    return render(request,'back/cat_list.html',context)


def cat_add(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        if name == "":
            error = "Your File Not Supported"
            return render(request, 'back/error.html', {'error': error})
        b = Cat(name=name)
        b.save()
        return redirect('cat_list')



    return render(request,'back/cat_add.html')