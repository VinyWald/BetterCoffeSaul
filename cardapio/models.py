from django.db import models

class Cardapio(models.Model):
    nome = models.CharField(max_length=200)

    tp = (
        ("ALL", "Todos"),
        ("C", "Comida"),
        ("B", "Bebida"),
    )
    tipo = models.CharField(max_length=50, choices=tp, default="ALL")
    
    promo = (
        ("S", "Sim"),
        ("N", "Nao"),
    )
    promocao = models.CharField(max_length=50, choices=promo, default="Nao")

    
    descricao = models.TextField(blank=True, null=True)  
    preco = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True) 
    foto = models.ImageField(upload_to='fotos_cardapio/',default="fotos_cardapio/default.png", blank=True, null=True)  

    
    
    adicionado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
