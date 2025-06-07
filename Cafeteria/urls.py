# Cafeteria/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Importe esta linha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), #
    path('cardapio/', include('cardapio.urls'),name="index"), #
    path('coffeoffice/', include('coffeoffice.urls')), #
    path('cart/', include('cart.urls', namespace='cart')), 
     path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    # Para servir arquivos estáticos (CSS, JS, etc.) durante o desenvolvimento
    urlpatterns += staticfiles_urlpatterns()
    # Para servir arquivos de mídia (uploads de usuários) durante o desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)