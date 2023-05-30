"""
    Este script adiciona algumas categorias no banco de dados usando alguns
    comandos do próprio django. Ainda não é possivel executar esse script 
    usando o comando 

        python adicionar_categoria.py

    Porém é possivel, mesmo assim, usar esse script para adicionar elementos no
    banco de dados, basta copiar e colar esses códigos no shell do django. Para
    acessar o shell do django basta usar o comando

        python manage.py shell
"""

from models import Categoria
from faker import Faker

# Lista de categorias
categorias = [
    'Fisica',
    'Quimica',
    'Programação',
    'Calculo',
    'Economia',
]

# objeto faker para gerar a descrição
fake = Faker()


for codigo, nome in enumerate(categorias, start=1):
    categoria = Categoria(
        cod_categoria = str(codigo).zfill(4),
        nome_categoria = nome,
        desc_categoria = fake.paragraph()
    )
    categoria.save()
