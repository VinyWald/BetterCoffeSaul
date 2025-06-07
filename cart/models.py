# cart/models.py
from django.db import models
from django.conf import settings
from cardapio.models import Cardapio # Assumindo que cardapio.models.Cardapio é seu produto principal
from coffeoffice.models import OfficeItem # Modelo que criamos na Parte 2

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Carrinho de {self.user.username if self.user.username else self.user.email}"

    def get_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.get_total_item_price()
        return total

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    # Para permitir tanto produtos do cardápio quanto itens de office no mesmo carrinho
    # Um deles será preenchido, o outro será None.
    cardapio_item = models.ForeignKey(Cardapio, on_delete=models.CASCADE, null=True, blank=True)
    office_item = models.ForeignKey(OfficeItem, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    # Preço no momento da adição, para evitar problemas se o preço do produto mudar
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_either_cardapio_or_office_item",
                check=(
                    models.Q(cardapio_item__isnull=False, office_item__isnull=True) |
                    models.Q(cardapio_item__isnull=True, office_item__isnull=False)
                ),
            )
        ]

    def __str__(self):
        if self.cardapio_item:
            return f"{self.quantity} x {self.cardapio_item.nome} no carrinho de {self.cart.user.username if self.cart.user.username else self.cart.user.email}"
        elif self.office_item:
            return f"{self.quantity} x {self.office_item.nome} no carrinho de {self.cart.user.username if self.cart.user.username else self.cart.user.email}"
        return "Item inválido no carrinho"

    @property
    def item_object(self):
        return self.cardapio_item if self.cardapio_item else self.office_item

    def get_item_price(self):
        if self.price_at_purchase is not None:
            return self.price_at_purchase
        return self.item_object.preco if self.item_object else 0

    def get_total_item_price(self):
        return self.quantity * self.get_item_price()