# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/cardapio/<int:item_id>/', views.add_to_cart, name='add_cardapio_item_to_cart'),
    path('add/office/<int:item_id>/', views.add_to_cart, name='add_office_item_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:cart_item_id>/', views.update_cart_item, name='update_cart_item'),
]