from django.db import models

# Model do usuário do tipo aluno
class Aluno(models.Model):
    matricula = models.CharField(max_length=6, blank=False, null=False, verbose_name='Matricula')
    nome = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome')
    cod_curso = models.CharField(max_length=3, blank=False, null=False, verbose_name='Código do Curso')
    # Campos de Endereço
    rua = models.CharField(max_length=50, blank=True, null=True, verbose_name='Rua')
    bairro = models.CharField(max_length=50, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cidade')
    estado = models.CharField(max_length=2, blank=True, null=True, verbose_name='Estado')
    cep = models.CharField(max_length=8, blank=True, null=True, verbose_name='CEP')
    # Fim de 'Campos de Endereço'
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Telefone/Celular')
    ingresso = models.DateField(blank=True, null=True, verbose_name='Data de Ingresso')
    conclusao = models.DateField(blank=True, null=True, verbose_name='Conclusão Prevista')

# Model do usuário do tipo Professor
class Professor(models.Model):
    siape = models.CharField(max_length=6, blank=False, null=False, verbose_name='SIAPE')
    nome = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome')
    # Campos de Endereço
    rua = models.CharField(max_length=50, blank=True, null=True, verbose_name='Rua')
    bairro = models.CharField(max_length=50, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cidade')
    estado = models.CharField(max_length=2, blank=True, null=True, verbose_name='Estado')
    cep = models.CharField(max_length=8, blank=True, null=True, verbose_name='CEP')
    # Fim de 'Campos de Endereço'
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Telefone/Celular')
    regime = models.CharField(blank=False, null=False, verbose_name='Regime de Trabalho')
    cod_curso = models.CharField(max_length=3, blank=False, null=False, verbose_name='Código do Curso')
    contratacao = models.DateField(blank=True, null=True, verbose_name='Data de Contratação')

# Model do usuário do tipo 'Funcionário'
class Funcionario(models.Model):
    matricula = models.CharField(max_length=6, blank=False, null=False, verbose_name='Matrícula')
    nome = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome')
    # Campos de Endereço
    rua = models.CharField(max_length=50, blank=True, null=True, verbose_name='Rua')
    bairro = models.CharField(max_length=50, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cidade')
    estado = models.CharField(max_length=2, blank=True, null=True, verbose_name='Estado')
    cep = models.CharField(max_length=8, blank=True, null=True, verbose_name='CEP')
    # Fim de 'Campos de Endereço'
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Telefone/Celular')