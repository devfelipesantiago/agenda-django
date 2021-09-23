from django.db import models
from django.contrib.auth.models import (
    User,
)  # Importa a tabela User criada pelo django

# Create your models here.


class Evento(models.Model):
    title = models.CharField(max_length=100)  # Max de 100 caractere
    description = models.TextField(
        blank=True, null=True
    )  # Pode ser branco e nulo
    data_evento = models.DateTimeField(
        verbose_name="data do evento"
    )  # nome da coluna
    data_criacao = models.DateTimeField(
        auto_now=True
    )  # Dato automatico, vai inserir o momento atual
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # Para mudar o nome da tabela
    # class Meta: db_table = 'evento'
    def __str__(self) -> str:
        return self.title
