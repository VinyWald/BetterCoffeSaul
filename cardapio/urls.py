
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index,name='indexCar'),
    path('adicionar/', views.adc,name='adicionar'),
    path('detalhes/<int:pk>',views.detalhes,name="detalhes"),
    path('all/', views.indexall,name='all'), 
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
