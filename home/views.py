from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm, CustomUserCreationForm # Adicione ReviewForm
from django.contrib import messages  # Importe o framework de mensagens

# --- VIEW INDEX CORRIGIDA ---
def index(request):
    # Busca as 3 últimas avaliações para exibir
    reviews = Review.objects.all()[:3]
    # Cria uma instância do formulário para ser usada no template
    review_form = ReviewForm()
    
    context = {
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, 'index.html', context)


# --- VIEW ADD_REVIEW CORRIGIDA ---
@login_required
def add_review(request):
    if request.method == 'POST':
        # Cria o formulário com os dados enviados
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Cria a instância da avaliação mas não salva no banco ainda
            review = form.save(commit=False)
            # Associa o usuário logado à avaliação
            review.user = request.user
            review.save()
            messages.success(request, 'Sua avaliação foi enviada com sucesso!')
            return redirect('cardapio:index')
        else:
            # Se o formulário for inválido, recarrega a página inicial
            # passando o formulário com os erros para que eles sejam exibidos.
            reviews = Review.objects.all()[:3]
            messages.error(request, 'Por favor, corrija os erros abaixo para enviar sua avaliação.')
            context = {
                'reviews': reviews,
                'review_form': form, # Passa o formulário com os erros
            }
            return render(request, 'index.html', context)
    
    # Se o método não for POST, simplesmente redireciona para a home
    return redirect('cardapio:index')

def signup_view(request):
    # ...
    pass
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Loga o usuário automaticamente após o cadastro
            return redirect('home:index')  # Redireciona para a home page ou LOGIN_REDIRECT_URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def meu_historico_view(request):
    # Lógica para buscar os pedidos do usuário logado.
    # Como o modelo de 'Pedido' ainda não foi criado,
    # vamos apenas renderizar a página por enquanto.
    pedidos = [] # Placeholder
    context = {
        'pedidos': pedidos
    }
    return render(request, 'home/meu_historico.html', context)

class PaginaEstaticaView(TemplateView):
    # Esta é uma view genérica para simplificar.
    # O template_name será definido na URL.
    pass