from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Aluno, Professor, Funcionario, Endereco
from django.http import Http404

# Create your views here.

# contantes
INDEX = 'index.html'
LOGIN = 'login.html'
ALUNO_INDEX = 'aluno_index.html'
PROFESSOR_INDEX = 'professor_index.html'
FUNCIONARIO_INDEX = 'funcionario_index.html'
ADMIN_INDEX = 'admin_index.html'
NOT_FOUND_404_INDEX = '404.html'
# contantes


def index(request):
    return render(request, INDEX)

def loginPage(request):
    return render(request, LOGIN)

@login_required(redirect_field_name='login')
def bibliotecaAluno(request):
    if request.method == 'GET':
        isAluno = Aluno.objects.filter(usuario__username = request.user.username)
        if isAluno:
            return render(request, ALUNO_INDEX)
        else:
            return render(request, NOT_FOUND_404_INDEX)

@login_required(redirect_field_name='login')
def bibliotecaProfessor(request):
    if request.method == 'GET':
        isProfessor = Professor.objects.filter(usuario__username = request.user.username)
        if isProfessor:
            return render(request, PROFESSOR_INDEX)
        else:
            return render(request, NOT_FOUND_404_INDEX)

@login_required(redirect_field_name='login')
def bibliotecaFuncionario(request):
    if request.method == 'GET':
        isFuncionario = Funcionario.objects.filter(usuario__username = request.user.username)
        if isFuncionario:
            if isFuncionario.first().isAdmin:
                return render(request, ADMIN_INDEX)
            else:
                return render(request, FUNCIONARIO_INDEX)
        else:
            return render(request, NOT_FOUND_404_INDEX)


@login_required(redirect_field_name='login')
def bibliotecaAdmin(request):
    return render(request, ADMIN_INDEX)

def login(request):
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(
            username = usuario,
            password = senha
        )

        if user:
            # Verificar se o usuário é um aluno
            aluno = Aluno.objects.filter(usuario__username = usuario) 
            if aluno:
                auth.login(request, user)
                return redirect('/biblioteca-aluno/')

            # Verificar se o usuário é um professor
            professor = Professor.objects.filter(usuario__username = usuario)
            if professor:
                auth.login(request, user)
                return redirect('/biblioteca-professor/')

            # Verificar de o usuário é um funcionário
            funcionario = Funcionario.objects.filter(usuario__username = usuario)
            if funcionario:
                auth.login(request, user)
                return redirect('/biblioteca-funcionario/')
                # Verificar se o usuário é um administrador, se sim, logar na ppagina de admin
                # se não, logar na página de funcionário comum
            pass
        else:
            # Retornar uma mensagem de erro
            pass
    
    else: 
        return render(request, LOGIN)
