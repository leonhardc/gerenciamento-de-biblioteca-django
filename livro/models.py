from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Model de app livro

class Livro(models.Model):
    isbn = models.CharField(max_length=13, blank=False, null=False, verbose_name='ISBN')
    titulo = models.CharField(max_length=200, blank=False, null=False, verbose_name='Titulo')
    ano_lancamento = models.CharField(max_length=4, blank=False, null=False, verbose_name='Ano de Lançamento')
    qt_copias = models.IntegerField(blank=False, null=False, verbose_name='Quantidade de Cópias')
    # TODO: Adicionar o campo de Autores

