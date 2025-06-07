# coffeoffice/models.py
from django.db import models
from django.utils import timezone

class OfficeItem(models.Model):
    ITEM_TYPE_CHOICES = [
        ('PROD', 'Produto de Papelaria'),
        ('SERV', 'Serviço de Escritório'),
    ]
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    tipo_item = models.CharField(max_length=4, choices=ITEM_TYPE_CHOICES, default='PROD')
    foto = models.ImageField(upload_to='fotos_office_items/', blank=True, null=True, default='fotos_office_items/default.png')
    disponivel = models.BooleanField(default=True)
    adicionado = models.DateTimeField(default=timezone.now)
    editado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome