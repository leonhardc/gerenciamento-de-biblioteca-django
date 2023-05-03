from django.db import models
from curso.models import Curso


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
    rua = models.CharField(max_length=50, blank=True, verbose_name='Rua')
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

# Model do usuário do tipo aluno
class Aluno(models.Model):
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
    nome = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    cod_curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, verbose_name='Código do Curso')
    endereco = models.OneToOneField(Endereco, null=True, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Telefone/Celular')
    ingresso = models.DateField(blank=True, null=True, verbose_name='Data de Ingresso')
    conclusao = models.DateField(blank=True, null=True, verbose_name='Conclusão Prevista')

# Model do usuário do tipo Professor
class Professor(models.Model):
    imagem = models.ImageField(
        upload_to='img/professor/%Y/%m/%d', 
        blank=True, 
        null=True, 
        verbose_name='Imagem'
    )
    siape = models.CharField(max_length=6, unique=True, blank=False, verbose_name='SIAPE')
    nome = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    endereco = models.OneToOneField(Endereco, null=True, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Telefone/Celular')
    regime = models.CharField(
        max_length=2, 
        choices=JORNADA,
        blank=False, 
        verbose_name='Regime de Trabalho'
    )
    cod_curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, verbose_name='Código do Curso')
    contratacao = models.DateField(blank=True, null=True, verbose_name='Data de Contratação')

# Model do usuário do tipo 'Funcionário'
class Funcionario(models.Model):
    imagem = models.ImageField(
        upload_to='img/funcionario/%Y/%m/%d', 
        blank=True, 
        null=True, 
        verbose_name='Imagem'
    )
    matricula = models.CharField(max_length=6, unique=True, blank=False, verbose_name='Matrícula')
    nome = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    endereco = models.OneToOneField(Endereco, null=True, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Telefone/Celular')