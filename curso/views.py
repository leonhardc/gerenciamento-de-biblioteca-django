from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.

def adicionar_curso(request):
    if request.method == 'POST':
        cod_curso = request.POST['cod_curso']
        nome_curso = request.POST['nome_curso']
        res_cod = Curso.objects.all(cod_curso=cod_curso)
        res_nome = Curso.objects.all(nome_curso=nome_curso)
        if res_cod or res_nome:
            messages.error(request, f'Curso {nome_curso} já existe na base de dados')
            return redirect('') # Retorna para página anterior com uma mensagem de erro
        else:
            novo_curso = Curso(
                cod_curso=cod_curso,
                nome_curso=nome_curso
            )
        novo_curso.save()
        messages.success(request, f'Curso {nome_curso} adicionado com sucesso')
        return redirect('') # Retorna para página anterior com uma mensagem de sucesso
    
def excluir_curso(request):
    if request.method == 'DELETE':
        cod_curso = request.DELETE['cod_curso']
        nome_curso = request.DELETE['nome_curso']
        res_cod = Curso.objects.all(cod_curso=cod_curso)
        res_nome = Curso.objects.all(nome_curso=nome_curso)
        if res_cod:
            res_cod.delete()
            messages.success(request, f'Curso {nome_curso} deletado com sucesso')
            return redirect('') # Retorna para página anterior com mensagem de sucesso
        elif res_nome:
            res_nome.delete()
            messages.success(request, f'Curso {nome_curso} deletado com sucesso')
            return redirect('') # Retorna para página anterior com mensagem de sucesso
        else:
            messages.error(request, f'O curso {nome_curso} não foi encontrado.')
            return redirect('') # Retornar para página anterior com mensagem de erro
    
def atualizar_curso(request):
    if request.method == 'UPDATE':
        cod_curso = request.UPDATE['cod_curso']
        nome_curso = request.UPDATE['nome_curso']
        res = Curso.objects.all(cod_curso=cod_curso)
        if res:
            res.nome_curso = nome_curso
            res.save()
            messages.success(request, f'Curso {nome_curso} atualizado com sucesso.')
            return redirect('') # Retorna para página anterior com mensagem de sucesso
        else:
            messages.error(request, f'Curso {nome_curso} não foi encontrado. Por favor verifique o codigo inserido e tente nomanente.')


    
