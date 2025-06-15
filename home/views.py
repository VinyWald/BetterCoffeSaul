from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm, CustomUserCreationForm # Adicione ReviewForm
from django.contrib import messages  # Importe o framework de mensagens
from .decorators import ssl_required


# --- VIEW INDEX CORRIGIDA ---
def index(request):
    # Busca as 3 últimas avaliações para exibir
    reviews = Review.objects.all()
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
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            # Envia uma mensagem de sucesso!
            messages.success(request, 'Obrigado pela sua avaliação!')
            return redirect('cardapio:index')
        else:
            # --- ESTA É A CORREÇÃO PRINCIPAL ---
            # Se o formulário for inválido, mostre os erros como mensagens.
            # Exemplo: "O campo de comentário não pode estar vazio."
            for field, errors in form.errors.items():
                for error in errors:
                    # Adiciona cada erro como uma mensagem de alerta
                    messages.error(request, f"{error}")
            
            # E então redireciona de volta, como antes.
            return redirect('cardapio:index')

    # Se não for POST, redireciona.
    return redirect('cardapio:index')
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            # --- MUDANÇA CRUCIAL ---
            # Redireciona para a página do CARDÁPIO, e não mais para a home.
            return redirect('cardapio:index') 

    # Se a requisição não for POST, também redireciona para a página do cardápio.
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