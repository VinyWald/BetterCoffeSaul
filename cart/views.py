# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse # Para atualizações AJAX se desejar no futuro
from .models import Cart, CartItem
from cardapio.models import Cardapio
from coffeoffice.models import OfficeItem
from django.urls import reverse


@login_required
def add_to_cart(request, item_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    item_type = None
    actual_item = None

    if 'cardapio' in request.resolver_match.url_name:
        item_type = 'cardapio'
        actual_item = get_object_or_404(Cardapio, id=item_id)
    elif 'office' in request.resolver_match.url_name:
        item_type = 'office'
        actual_item = get_object_or_404(OfficeItem, id=item_id)

    if not actual_item:
        # Lidar com erro ou redirecionar
        return redirect(request.META.get('HTTP_REFERER', '/'))

    cart_item = None
    if item_type == 'cardapio':
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            cardapio_item=actual_item,
            office_item=None,
            defaults={'price_at_purchase': actual_item.preco}
        )
    elif item_type == 'office':
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            cardapio_item=None,
            office_item=actual_item,
            defaults={'price_at_purchase': actual_item.preco}
        )

    if not item_created:
        cart_item.quantity += 1
    # Sempre atualize o preço no momento da compra se o item já existia e foi adicionado novamente
    # ou se você quiser que o preço seja sempre o atual do produto (decisão de design)
    cart_item.price_at_purchase = actual_item.preco 
    cart_item.save()

    return redirect('cart:view_cart')



def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {'cart': cart}
    return render(request, 'cart/cart_detail.html', context)


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart:view_cart')


def update_cart_item(request, cart_item_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        try:
            quantity = int(quantity)
            if quantity > 0:
                cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
                cart_item.quantity = quantity
                cart_item.save()
            elif quantity == 0: # Remover se a quantidade for 0
                cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
                cart_item.delete()
        except (ValueError, TypeError):
            pass # Lidar com erro de quantidade inválida
    return redirect('cart:view_cart')