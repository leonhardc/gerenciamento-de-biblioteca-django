from usuario.models import Funcionario, Endereco
from curso.models import Curso
from django.contrib.auth.models import User
from unidecode import unidecode
from faker import Faker
import random
import string
import re
import datetime

fake = Faker('pt_BR')

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
        if tipo == 'Aluno':
            nome_arquivo = 'alunos.txt'            
        elif tipo == 'Professor':
            nome_arquivo = 'professores.txt'
        elif tipo == 'Funcionario':
            nome_arquivo = 'funcionarios.txt'
        line = f"Usuario: {username} / Senha: {senha} (Usuario_{tipo})"
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.writelines(line + '\n')
        ## Verificar se o usuário criado já existe na base de dados
        user_django = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user_django.set_password(senha)
        user_django.save()
        return user_django
    else:
        return None


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
        print('Concluido ... ')
    # fim da função loadBarr()
    
def main():
    qt_alunos = 40
    sucessos = 0
    erros = 0
    print('Adicionando funcionarios na base de dados...')
    for _ in range(qt_alunos):
        loadBarr(_, qt_alunos-1)
        adicionou = adicionar_funcionario()
        if adicionou:
            sucessos += 1
        else:
            erros += 1
    print(f'{sucessos} funcionarios adicionados. {erros} funcionarios não adicionados.')


def delete_users():
    # Função usada para deletar usuarios que não são alunos, professores ou usuários, exceto o 'admin'
    from usuario.models import Aluno, Funcionario, Professor
    all_users = User.objects.all()
    users_deleted = 0
    for user in all_users:
        isAluno = Aluno.objects.filter(usuario__username=user.username).exists()
        isProfessor = Professor.objects.filter(usuario__username=user.username).exists()
        isFuncionario = Funcionario.objects.filter(usuario__username=user.username).exists()
        if isAluno or isProfessor or isFuncionario or user.username == 'admin':
            pass
        else:
            print(user, ' foi deletado.')
            users_deleted += 1
            user.delete()
    print()
    print(users_deleted, ' foram deletados.')