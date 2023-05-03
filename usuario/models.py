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
    
    # Método para redimensionar o tamanho da imagem de perfil para otimizar espaço no banco de dados
    @staticmethod
    def redimensionar_imagem(img, max_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        image_pil = Image.open(img_full_path)
        original_width, original_height = image_pil.size 
        
        if original_width <= max_width:
            image_pil.close() 
            return

        new_height = round((max_width * original_height) / original_width) 
        new_image = image_pil.resize((max_width, new_height), Image.LANCZOS) 
        new_image.save(         
            img_full_path,   
            optimize=True,
            quality=50  
        )

    # Representação do Objeto
    def __str__(self) -> str:
        return f'Aluno: {self.matricula} - {self.nome}'
    
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

    # Método para redimensionar imagem
    @staticmethod
    def redimensionar_imagem(img, max_width=800):

        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        image_pil = Image.open(img_full_path)
        original_width, original_height = image_pil.size 
        if original_width <= max_width:
            image_pil.close() 
            return

        new_height = round((max_width * original_height) / original_width) 
        new_image = image_pil.resize((max_width, new_height), Image.LANCZOS) 
        new_image.save(         
            img_full_path,   
            optimize=True,
            quality=50  
        )

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

    # Método para redimensionar imagem
    @staticmethod
    def redimensionar_imagem(img, max_width=800):

        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        image_pil = Image.open(img_full_path)
        original_width, original_height = image_pil.size 
        if original_width <= max_width:
            image_pil.close() 
            return

        new_height = round((max_width * original_height) / original_width) 
        new_image = image_pil.resize((max_width, new_height), Image.LANCZOS) 
        new_image.save(         
            img_full_path,   
            optimize=True,
            quality=50  
        )

    # Representação do objeto
    def __str__(self) -> str:
        return f'Funcionário: {self.matricula} - {self.nome}'
    
    # Representação do objeto na zona administrativa
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'