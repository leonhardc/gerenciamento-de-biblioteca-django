from django.shortcuts import render
from .models import Autor, Categoria, Livro


LIVROS = 'livros.html'

def busca_livros(request):
    if request.method == 'GET':
        pass

def lista_livros(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        return render(
            request,
            template_name=LIVROS,
            context={'livros': livros}
        )
