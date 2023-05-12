from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from .models import Aluno, Professor, Funcionario, Endereco

# Create your views here.

# contantes
INDEX = 'index.html'
LOGIN = 'login.html'
ALUNO_INDEX = 'aluno_index.html'
PROFESSOR_INDEX = 'professor_index.html'
FUNCIONARIO_INDEX = 'funcionario_index.html'
ADMIN_INDEX = 'admin_index.html'
# contantes

def index(request):
    return render(request, INDEX)

def loginPage(request):
    return render(request, LOGIN)

def bibliotecaAluno(request):
    return render(request, ALUNO_INDEX)

def bibliotecaProfessor(request):
    return render(request, PROFESSOR_INDEX)

def bibliotecaFuncionario(request):
    return render(request, FUNCIONARIO_INDEX)

def bibliotecaAdmin(request):
    return render(request, ADMIN_INDEX)

def login(request):

    if request.method != 'POST':
        # Adicionar mensagem de erro
        return render(request, LOGIN)

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    print(f'<usuario: ', usuario, '; senha: ', senha, '>')

    usuario = authenticate(
        username = usuario,
        password = senha
    )

    if usuario is not None:
        # Verificar se o usuário é um aluno

        aluno = Aluno.objects.get(usuario = usuario) 
        if aluno is not None:
            # auth.login(request, usuario)
            return redirect('/biblioteca-aluno/')

        # Verificar se o usuário é um professor
        professor = Professor.objects.get(usuario = usuario)
        if professor is not None:
            return redirect('/biblioteca-professor/')

        # Verificar de o usuário é um funcionário
        funcionario = Funcionario.objects.get(usuario = usuario)
        if funcionario is not None:
            return redirect('/biblioteca-funcionario/')
            # Verificar se o usuário é um administrador, se sim, logar na ppagina de admin
            # se não, logar na página de funcionário comum
        pass
    else:
        # Retornar uma mensagem de erro
        pass
