from django.contrib.auth.models import User
from django.conf import settings
from curso.models import Curso
from django.db import models
from PIL import Image
import os


JORNADA = (
    ('20', '20hr'),
    ('40', '40hr'),
    ('DE', 'DE'),
)

ESTADOS = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)

# Model compartilhado por todas as classes abaixo, que é o endereço
class Endereco(models.Model):

    usuario = models.OneToOneField(User, verbose_name='Usuario', on_delete=models.CASCADE)

    rua = models.CharField(max_length=50, blank=True, verbose_name='Rua')
    numero = models.CharField(max_length=6, blank=True, verbose_name='Numero')
    bairro = models.CharField(max_length=50, blank=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, blank=True, verbose_name='Cidade')
    estado = models.CharField(
        max_length=2, 
        blank=True, 
        choices=ESTADOS, 
        default='CE',
        verbose_name='Estado'
    )
    cep = models.CharField(max_length=8, blank=True, verbose_name='CEP')
    complemento = models.CharField(max_length=150, blank=True, verbose_name='Complemento')

    def __str__(self) -> str:
        return f'{self.rua}, {self.numero}, {self.bairro}, {self.cidade}, {self.estado}, {self.cep}'

# Model do usuário do tipo aluno
class Aluno(models.Model):

    usuario = models.OneToOneField(User, verbose_name='Usuario/Aluno', on_delete=models.CASCADE)
    imagem = models.ImageField(
        upload_to='img/aluno/%Y/%m/%d', 
        blank=True, 
        null=True, 
        verbose_name='Imagem'
    )
    matricula = models.CharField(
        max_length=6, 
        unique=True, 
        blank=False, 
        verbose_name='Matricula'
    )
    cod_curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, verbose_name='Código do Curso')
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Telefone/Celular')
    ingresso = models.DateField(blank=True, null=True, verbose_name='Data de Ingresso')
    conclusao = models.DateField(blank=True, null=True, verbose_name='Conclusão Prevista')

    # Representação do Objeto
    def __str__(self) -> str:
        return f'Aluno: {self.matricula} - {self.usuario.first_name} {self.usuario.last_name}'
    
    # Representação da classe na area administrativa
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
    
# Model do usuário do tipo Professor
class Professor(models.Model):

    usuario = models.OneToOneField(User, verbose_name='Usuario/Professor', on_delete=models.CASCADE)

    imagem = models.ImageField(
        upload_to='img/professor/%Y/%m/%d', 
        blank=True, 
        null=True, 
        verbose_name='Imagem'
    )
    siape = models.CharField(max_length=6, unique=True, blank=False, verbose_name='SIAPE')
    nome = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Telefone/Celular')
    regime = models.CharField(
        max_length=2, 
        choices=JORNADA,
        blank=False, 
        verbose_name='Regime de Trabalho'
    )
    cod_curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, verbose_name='Código do Curso')
    contratacao = models.DateField(blank=True, null=True, verbose_name='Data de Contratação')

    # Representação do objeto
    def __str__(self) -> str:
        return f'Professor: {self.matricula} - {self.nome}'
    
    # Representação do objeto na area administrativa
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

# Model do usuário do tipo 'Funcionário'
class Funcionario(models.Model):

    usuario = models.OneToOneField(User, verbose_name='Usuario/Funcionario', on_delete=models.CASCADE)

    imagem = models.ImageField(
        upload_to='img/funcionario/%Y/%m/%d', 
        blank=True, 
        null=True, 
        verbose_name='Imagem'
    )
    matricula = models.CharField(max_length=6, unique=True, blank=False, verbose_name='Matrícula')
    nome = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Telefone/Celular')

    # Representação do objeto
    def __str__(self) -> str:
        return f'Funcionário: {self.matricula} - {self.nome}'
    
    # Representação do objeto na zona administrativa
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'