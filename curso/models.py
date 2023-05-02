from django.db import models

class Curso(models.Model):
    cod_curso = models.CharField(max_length=3, blank=False, null=False, verbose_name='Codigo do Curso')
    nome_curso = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nome do Curso')
