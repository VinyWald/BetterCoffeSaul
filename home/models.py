# home/models.py
from django.db import models
from django.conf import settings # Para referenciar o modelo de usuário

# Create your models here.

class Review(models.Model):
    # Relaciona a avaliação ao usuário que a fez
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Guarda a nota de 1 a 5
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    
    # O comentário em texto
    comment = models.TextField(max_length=500)
    
    # Data de criação
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Avaliação de {self.user.username} - {self.rating} estrelas'

    class Meta:
        ordering = ['-created_at'] # Ordena as avaliações da mais nova para a mais antiga