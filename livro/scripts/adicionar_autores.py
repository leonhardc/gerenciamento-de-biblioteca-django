"""
    Executar esse script no shell do django
"""

from livro.models import Autor
from faker import Faker

fake = Faker()

# Adicionar cerca de 50 autores no banco de dados
for _ in range(50):
    autor = Autor(
        nome = fake.name(),
        cpf = fake.random_number(digits=11),
        nacionalidade = fake.country() 
    )
    autor.save()
