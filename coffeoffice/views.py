from django.shortcuts import render
from . models import Op


# Create your views here.

def index (request):
    tp = Op.objects.all()
    context={
        'lista':tp
    }
    return render(request,'coffeoffice.html',context)