# Importações
from curso.models import Curso
from livro.models import Livro, Categoria, Autor
from usuario.models import Aluno, Professor, Funcionario, Endereco
from django.contrib.auth.models import User
from faker import Faker
import random
from unidecode import unidecode
import string
import re
import datetime
import os

# Variaveis globais
fake = Faker()
cursos = [
    'Ciências Econômicas',
    'Engenharia de Computação',
    'Engenharia Elétrica',
    'Finanças',
    'Medicina',
    'Música',
    'Odontologia',
    'Psicologia',
]
categorias = [
    'Fisica',
    'Quimica',
    'Programação',
    'Calculo',
    'Economia',
]

# Funções para adicionar cursos
def adicionar_curso(codigo, curso):
    if Curso.objects.filter(nome_curso=curso).exists():
        return False    
    curso_obj = Curso(cod_curso=str(codigo).zfill(3), nome_curso=curso)
    curso_obj.save()
    return True

# Funções para adicionar livros

## Autores de livros
def adicionar_autor():
    autor = Autor(
        nome=fake.name(),
        cpf=fake.random_number(digits=11),
        nacionalidade=fake.country() 
    )
    if not autor:
        return False
    autor.save()
    return True

## Categorias de livros
def adicionar_categoria(codigo, categoria):
    if Categoria.objects.filter(nome_categoria=categoria).exists():
        return False
    categoria_obj = Categoria(
        cod_categoria = str(codigo).zfill(4),
        nome_categoria = categoria,
        desc_categoria = fake.paragraph()
    )
    categoria_obj.save()
    return True

## Livros
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

def adicionar_livro():
    autores = buscar_autores()
    categorias = buscar_categorias()
    livro = Livro(
        isbn = gerar_isbn(),
        titulo = fake.catch_phrase() + " " + fake.word() + " " + fake.word(),
        ano_lancamento = str(random.randint(1950, 2023)), 
        qt_copias = random.randint(10, 30)
    )
    if not livro:
        return False
    livro.save()
    for autor in autores:
        livro.autores.add(autor)
    for categoria in categorias:
        livro.categoria.add(categoria)
    livro.save()
    return True

# Adicionar usuários Alunos, Professores e Funcionarios

# Funções auxiliares
def gerar_senha(tamanho=8):
    # gerar uma senha aleatoria de 8 digitos
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def remover_acentos(texto):
    return unidecode(texto)

def adicionar_usuario(tipo):
    # gerar um usuário e adicioná-lo em uma base de dados e no banco de dados
    name_list = fake.name().split(" ")
    remover = ['dr.', 'dra.', 'sr.', 'sra.']
    # retirar as abreviações acima dos nomes proprios
    for rem in remover:
        name_list = [name for name in name_list if name.lower() != rem]
    # Caracteristicas do usuário
    username = re.sub('[^a-zA-Z0-9]', '', name_list[0] + '_' + name_list[1])
    first_name = name_list[0]
    last_name = " ".join(name_list[1:])
    email = remover_acentos(name_list[0].lower()) + "_" + remover_acentos(name_list[1].lower()) + "@email.com"
    senha = gerar_senha()
    # Criando usuário no django
    usuario_existe = User.objects.filter(username=username).exists()
    if not usuario_existe:
        # Salvando usuário e senha em um arquivo
        nome_arquivo = 'alunos.txt'
        line = '{0:<15}|{1:^30}|{2:^10}'.format(tipo, username, senha)
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.writelines(line + '\n')
        ## Verificar se o usuário criado já existe na base de dados
        user_django = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user_django.set_password(senha)
        user_django.save()
        return user_django
    else:
        return None

def gerar_endereco():
    fake = Faker('pt_BR')
    endereco = fake.address().replace('\n', ', ')
    return endereco

def gerar_endereco_brasileiro():
    fake = Faker('pt_BR')
    endereco = fake.address()
    rua_numero, bairro, cep_cidade_estado = endereco.split('\n')
    if ',' in rua_numero:
        rua, numero = rua_numero.split(',')
    else:
        rua = rua_numero
        numero = 'SN'
    cep_cidade, estado = cep_cidade_estado.split('/')
    cep = ''
    cidade = ''
    for char in cep_cidade:
        if char.isnumeric():
            cep += char
        elif char.isalpha() or char == ' ':
            cidade += char 
    endereco_dict = {
        'rua': rua.strip(),
        'numero': numero.strip(),
        'bairro': bairro.strip(),
        'cep': cep.strip(),
        'cidade': cidade.strip(),
        'estado': estado.strip(),
    }
    return endereco_dict

def gerar_datas():
    # Gerar datas de inicio e fim do curso
    ano = random.randint(2015, 2023)
    datas_dict = {
        'data_inicio': datetime.date(ano, 1, 1),
        'data_fim': datetime.date(ano+4, 12, 31)
    }
    return datas_dict

def gerar_matricula():
    return str(random.randint(111111, 999999))

def gerar_numero_telefone():
    ddd = random.randint(11, 99)  # Gera um DDD entre 11 e 99
    parte1 = random.randint(1000, 9999)  # Gera a primeira parte do número (4 dígitos)
    parte2 = random.randint(1000, 9999)  # Gera a segunda parte do número (4 dígitos)    
    numero_telefone = f"({ddd}) {parte1}-{parte2}"
    return numero_telefone

def loadBarr(estado_atual, estado_final):
    # estado_final: numero inteiro que guarda o numero total de amostras do
    # conjunto de amostras que está sendo avaliado
    # estado_inicial: numero inteiro que armazena o indice atual da amostra que
    # está sendo processada
    # estado_atual não pode nunca ser maior que estado_final    
    etapa = (estado_atual/estado_final)*100
    str_etapa = ''
    str_saida = '\r'
    for i in  range(1, 101):
        if i<etapa and i%2:            
            str_etapa = str_etapa + '*'
    str_saida = '\r[' + str_etapa + '] ' + str(int(etapa)) + '%'
    print(str_saida, end = '')  
    if etapa == 100:
        print('\n')
    # fim da função loadBarr()

# Adicionar aluno
def adicionar_aluno():
    usuario_aluno = adicionar_usuario('Aluno') # Adicionando o usuário na base de dados
    if not usuario_aluno:
        return False
    endereco_dict = gerar_endereco_brasileiro() # Definindo o endereco do aluno
    endereco_aluno = Endereco(
        usuario = usuario_aluno,
        rua = endereco_dict['rua'],
        numero = endereco_dict['numero'],
        bairro = endereco_dict['bairro'],
        cidade = endereco_dict['cidade'],
        estado = endereco_dict['estado'],
        cep = endereco_dict['cep'],
        complemento = "..."
    )
    endereco_aluno.save()
    cursos = Curso.objects.all() # Escolhendo o curso do aluno
    curso_aluno = cursos[random.randint(0, len(cursos)-1)]
    data_inicio_fim = gerar_datas()
    aluno = Aluno( # Definindo o objeto aluno
        usuario = usuario_aluno,
        cod_curso = curso_aluno,
        matricula = gerar_matricula(),
        telefone = gerar_numero_telefone(),
        ingresso = data_inicio_fim['data_inicio'],
        conclusao = data_inicio_fim['data_fim']
    )
    aluno.save()
    return True

# Adicionar professor
def adicionar_professor():
    usuario_professor = adicionar_usuario('Professor')
    if not usuario_professor:
        return False
    regime = ['20', '40', 'DE']
    cursos = Curso.objects.all()
    datas = gerar_datas()
    siape = gerar_matricula()
    nome_professor = usuario_professor.first_name + usuario_professor.last_name
    telefone_professor = gerar_numero_telefone()
    regime_professor = regime[random.randint(0, len(regime)-1)]
    curso_professor = cursos[random.randint(0, len(cursos)-1)]
    contratacao = datas['data_inicio']
    endereco = gerar_endereco_brasileiro()
    endereco_professor = Endereco(
        usuario=usuario_professor,
        rua=endereco['rua'],
        numero=endereco['numero'],
        bairro=endereco['bairro'],
        cidade=endereco['cidade'],
        estado=endereco['estado'],
        cep=endereco['cep'],
        complemento=''
    )
    endereco_professor.save()
    professor = Professor(
        usuario=usuario_professor,
        siape=siape,
        nome=nome_professor,
        telefone=telefone_professor,
        regime=regime_professor,
        cod_curso=curso_professor,
        contratacao=contratacao
    )
    professor.save()
    return True

# Adicionar Funcionario
def adicionar_funcionario():
    usuario_funcionario = adicionar_usuario('Funcionario')
    if not usuario_funcionario:
        return False
    endereco = gerar_endereco_brasileiro()
    endereco_funcionario = Endereco(
        usuario=usuario_funcionario,
        rua=endereco['rua'],
        numero=endereco['numero'],
        bairro=endereco['bairro'],
        cidade=endereco['cidade'],
        estado=endereco['estado'],
        cep=endereco['cep'],
        complemento=''
    )
    endereco_funcionario.save()
    nome_funcionario = usuario_funcionario.first_name + ' ' + usuario_funcionario.last_name
    matricula = gerar_matricula()
    telefone_funcionario = gerar_numero_telefone()
    funcionario = Funcionario(
        usuario=usuario_funcionario,
        matricula=matricula,
        nome=nome_funcionario,
        telefone=telefone_funcionario,
        isAdmin=False
    )
    funcionario.save()
    return True

def excluir_arquivos():
    alunos = 'alunos.txt'
    professores = 'professores.txt'
    funcionarios = 'funcionarios.txt'

    if os.path.isfile(alunos):
        os.remove(alunos)

    if os.path.isfile(professores):
        os.remove(professores)
    
    if os.path.isfile(funcionarios):
        os.remove(funcionarios)
    

# Função principal
def main():
    # Excluindo, se existirem, os arquivos 'alunos.txt', 'professores.txt' e 'funcionarios.txt'
    excluir_arquivos()

    # Adiciona Cursos, Livros, Autores, Categorias, Alunos, Professores, Funcionarios e Endereços no banco de dados
    num_autores = 50
    num_livros = 200
    num_alunos = 200
    num_professores = 50
    num_funcionarios = 30
    # Adicionando cursos na base de dados
    print('Adicionando Cursos na base de dados ...')
    sucessos = 0
    falhas = 0
    for codigo, nome in enumerate(cursos, start=1):
        add = adicionar_curso(codigo, nome)
        loadBarr(codigo, len(cursos))
        if add:
            sucessos+=1
        else:
            falhas+=1
    print(f'{sucessos} cursos adicionados com sucesso. {falhas} falhas.')

    # Adicionando Autores na base de dados
    sucessos = 0
    falhas = 0
    for _ in range(num_autores):
        add = adicionar_autor()
        loadBarr(_, num_autores)
        if add:
            sucessos+=1
        else:
            falhas+=1
    print(f'{sucessos} autores adicionados com sucesso. {falhas} falhas.')

    # Adicionando categorias na base de dados
    sucessos = 0
    falhas = 0
    for codigo, nome in enumerate(categorias, start=1):
        add = adicionar_categoria(codigo, nome)
        loadBarr(codigo, len(categorias))
        if add:
            sucessos+=1
        else:
            falhas+=1
    print(f'{sucessos} categorias adicionadas com sucesso. {falhas} falhas.')

    # Adicionando livros
    sucessos = 0
    falhas = 0
    for _ in range(num_livros):
        add = adicionar_livro()
        loadBarr(_, num_livros)
        if add:
            sucessos+=1
        else:
            falhas+=1
    print(f'{sucessos} livros adicionados com sucesso. {falhas} falhas.')

    # Adicionando alunos
    sucessos = 0
    falhas = 0
    for _ in range(num_alunos):
        add = adicionar_aluno()
        loadBarr(_, num_alunos)
        if add:
            sucessos+=1
        else:
            falhas+=1
    print(f'{sucessos} alunos adicionados com sucesso. {falhas} falhas.')

    # Adicionando professores
    sucessos = 0
    falhas = 0
    for _ in range(num_professores):
        add = adicionar_professor()
        loadBarr(_, num_professores)
        if add:
            sucessos+=1
        else:
            falhas+=1
    print(f'{sucessos} professores adicionados com sucesso. {falhas} falhas.')

    # Adicionando funcionarios
    sucessos = 0
    falhas = 0
    for _ in range(num_funcionarios):
        add = adicionar_funcionario()
        loadBarr(_, num_funcionarios)
        if add:
            sucessos+=1
        else:
            falhas+=1
    print(f'{sucessos} funcionarios adicionados com sucesso. {falhas} falhas.')