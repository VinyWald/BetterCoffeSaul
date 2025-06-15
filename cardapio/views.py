from django.http import Http404
from django.shortcuts import render, redirect
from . forms import CarForm
from . models import Cardapio
from home.models import Review      # Supondo que seu app se chama 'home'
from home.forms import ReviewForm   # Supondo que seu app se chama 'home'
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Importe o framework de mensagens

def index(request):
    # 1. Busca os dados do cardápio (como já fazia)
    cardapio_items = Cardapio.objects.all()

    # 2. Busca TODAS as avaliações do app 'home', ordenando pelas mais recentes
    all_reviews = Review.objects.all().order_by('-created_at')

    # 3. Cria uma instância do formulário de avaliação para ser exibida na página
    review_form = ReviewForm()

    # 4. Cria o contexto com TODOS os dados que o template precisa
    context = {
        'lista': cardapio_items,       # 'lista' para o loop do cardápio
        'reviews': all_reviews,      # 'reviews' para o loop das avaliações
        'review_form': review_form,  # 'review_form' para o formulário de envio
    }
    
    # Renderiza o template 'car.html' com todo o contexto combinado
    return render(request, 'car.html', context)
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