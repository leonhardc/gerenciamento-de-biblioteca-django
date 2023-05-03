from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autor.models import Autor


class Categoria(models.Model):
    cod_categoria = models.CharField(max_length=4, blank=False, unique=True, verbose_name='Código da Categoria')
    nome_categoria = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome da Categoria')
    desc_categoria = models.TextField(max_length=500, blank=True, null=True, verbose_name='Descrição')

# Model de app livro
class Livro(models.Model):
    isbn = models.CharField(max_length=13, blank=False, unique=True, verbose_name='ISBN')
    titulo = models.CharField(max_length=200, blank=False, null=False, verbose_name='Titulo')
    ano_lancamento = models.CharField(max_length=4, blank=False, null=False, verbose_name='Ano de Lançamento')
    qt_copias = models.IntegerField(blank=False, null=False, verbose_name='Quantidade de Cópias')
    autores = models.ManyToManyField(Autor, verbose_name='Autores')
    categoria = models.ManyToManyField(Categoria, verbose_name='Categoria')

