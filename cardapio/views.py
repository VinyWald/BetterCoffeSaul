from django.http import Http404
from django.shortcuts import render
from . forms import CarForm
from . models import Cardapio

# Create your views here.

def index (request):
    car = Cardapio.objects.all()
    context={
        'lista':car
    }
    return render(request,'car.html',context)

def indexall (request):
    car = Cardapio.objects.all()
    context={
        'lista':car
    }
    return render(request,'all.html',context)

def adc(request):
    form=CarForm(request.POST)
    if request.method =="POST":
        form=CarForm(request.POST)
        
        if form.is_valid():
            post=form.save()
            post.save()
            form=CarForm()
            return render(request,'adc_car.html',{'form':form})
        else:
            form=CarForm()
    return render(request,'adc_car.html',{'form':form})

def detalhes(request,pk):
    print("Primary Key {}".format(pk))
    try:
        car=Cardapio.objects.filter(pk=pk)
        print(car.values())
    except car.DoesNotExist:
        raise Http404('Produto não existe')
    
    context={
        'car':car
    }
    return render(request,'detalhes.html',context)