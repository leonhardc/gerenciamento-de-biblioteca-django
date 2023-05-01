from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False, verbose_name='Nome')
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF')
    nacionalidade = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nacionalidade')