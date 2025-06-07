# coffeoffice/views.py
from django.shortcuts import render
from .models import OfficeItem

def office_list(request):
    items = OfficeItem.objects.filter(disponivel=True)
    context = {'office_items': items}
    return render(request, 'coffeoffice/office_list.html', context)

# A view 'index' original pode ser removida ou adaptada se não for mais usada.
# def index(request):
#     return render(request, "coffeoffice.html")