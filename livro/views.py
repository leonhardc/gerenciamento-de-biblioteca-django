from django.shortcuts import render
from .models import Autor, Categoria, Livro


LIVROS = 'livros.html'

def lista_livros(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        return render(
            request,
            template_name=LIVROS,
            context={'livros': livros}
        )

# TODO; Implementar view para buscar livros
def busca_livros(request):
    if request.method == 'GET':
        pass

# TODO: Implementar view de inserir livros
def insere_livro(request):
    if request.method == 'POST':
        ... 

# TODO: Implementar view de excluir livro
def excluir_livro(request):
    ...

# TODO: Implementar view de listar autores
def lista_autores(request):
    ...

# TODO> Implementar view de inserir Autor
def inserir_autor(request):
    if request.method == 'POST':
        ...

# TODO: Implementar view de excluir autor
def excluir_autor(request):
    ...

# TODO: Implementar view que lista categorias
def lista_categorias(request):
    ...

# TODO: Inserir view de inserir categorias
def inserir_categoria(request):
    if request.method == 'POST':
        ...

#  TODO: Inserir view de excluir categorias
def excluir_categoria(request):
    ...

# TODO: Implementar view para realizar uma reserva
def fazer_reserva(request):
    if request.method == 'POST':
        ...

# TODO: Implementar view para excluir reserva
def excluir_reserva(request):
    ...

# TODO: Implementar view para adicionar um novo emprestimo no banco de dados
def fazer_emprestimo(request):
    ...

# TODO: Implementar view para dar baixa em empestimo no banco de dados
def excluir_emprestimo(request):
    ...