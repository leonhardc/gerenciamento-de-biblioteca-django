from livro.models import Livro, Categoria, Autor
import random
from faker import Faker

fake = Faker()

def gerar_isbn():
    return ''.join(str(random.randint(0, 9)) for _ in range(13))

def buscar_autores():
    autores = Autor.objects.all()
    num_autores = random.randint(1,4)
    lista_autores = []
    for _ in range(num_autores):
        lista_autores.append(
            autores[random.randint(0, len(autores)-1)]
        )
    return lista_autores

def buscar_categorias():
    categorias = Categoria.objects.all()
    num_categorias = random.randint(1,3)
    lista_categorias = []
    for _ in range(num_categorias):
        lista_categorias.append(
            categorias[random.randint(0, len(categorias)-1)]
        )
    return lista_categorias

for _ in range(150):
    num_autores = random.randint(1, 4)
    autores = buscar_autores()
    categorias = buscar_categorias()
    livro = Livro(
        isbn = gerar_isbn(),
        titulo = fake.catch_phrase() + " " + fake.word() + " " + fake.word(),
        ano_lancamento = str(random.randint(1950, 2023)), 
        qt_copias = random.randint(10, 30)
    )
    livro.save()
    for autor in autores:
        livro.autores.add(autor)
    for categoria in categorias:
        livro.categoria.add(categoria)
    livro.save()
    