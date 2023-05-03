from django.db import models

class Curso(models.Model):
    cod_curso = models.CharField(max_length=3, blank=False, verbose_name='Codigo do Curso')
    nome_curso = models.CharField(max_length=50, blank=False, verbose_name='Nome do Curso')

    def __str__(self) -> str:
        return f'{self.cod_curso} - ({self.nome_curso})'
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'