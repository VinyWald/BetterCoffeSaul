# coffeoffice/urls.py
from django.urls import path
from . import views

app_name = 'coffeoffice'

urlpatterns = [
    path('', views.office_list, name='office_list'),
    # path('index/', views.index, name='index'), # Se ainda precisar da antiga 'index'
]