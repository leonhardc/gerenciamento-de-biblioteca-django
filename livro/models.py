from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Autor(models.Model):
    nome = models.CharField(max_length=200, blank=False, verbose_name='Nome')
    cpf = models.CharField(max_length=11, blank=False, unique=True, verbose_name='CPF')
    nacionalidade = models.CharField(max_length=50, blank=False, verbose_name='Nacionalidade')

    def __str__(self) -> str:
        return f'{self.nome}, {self.nacionalidade}'

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Categoria(models.Model):
    cod_categoria = models.CharField(max_length=4, blank=False, unique=True, verbose_name='Código da Categoria')
    nome_categoria = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome da Categoria')
    desc_categoria = models.TextField(max_length=500, blank=True, null=True, verbose_name='Descrição')

    def __str__(self) -> str:
        return f'{self.cod_categoria} - {self.nome_categoria}'

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

# Model de app livro
class Livro(models.Model):
    isbn = models.CharField(max_length=13, blank=False, unique=True, verbose_name='ISBN')
    titulo = models.CharField(max_length=200, blank=False, null=False, verbose_name='Titulo')
    ano_lancamento = models.CharField(max_length=4, blank=False, null=False, verbose_name='Ano de Lançamento')
    qt_copias = models.IntegerField(blank=False, null=False, verbose_name='Quantidade de Cópias')
    autores = models.ManyToManyField(Autor, verbose_name='Autores')
    categoria = models.ManyToManyField(Categoria, verbose_name='Categoria')

    def __str__(self) -> str:
        return f'{self.titulo}'

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

#  Model de reservas de livros
class Reservas(models.Model):
    usuario = models.ManyToManyField(User, verbose_name='Usuario')
    livro = models.ManyToManyField(Livro, verbose_name='livro')
    data_reserva = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

