from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'home' # Adicione se ainda não tiver, para namespacing

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'), # Nova URL para cadastro
      path(
        'termos-e-condicoes/', 
        TemplateView.as_view(template_name='home/termos_e_condicoes.html'), 
        name='termos_e_condicoes'
    ),
    path(
        'politica-de-privacidade/', 
        TemplateView.as_view(template_name='home/politica_de_privacidade.html'), 
        name='politica_de_privacidade'
    ),
    path(
        'central-de-ajuda/', 
        TemplateView.as_view(template_name='home/central_de_ajuda.html'), 
        name='central_de_ajuda'
    ),
    path('meu-historico/', views.meu_historico_view, name='meu_historico'),
    path('add_review/', views.add_review, name='add_review'),
]