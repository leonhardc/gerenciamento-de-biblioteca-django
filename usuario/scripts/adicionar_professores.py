from usuario.models import Professor, Endereco
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
    qt_alunos = 50
    sucessos = 0
    erros = 0
    print('Adicionando alunos na base de dados...')
    for _ in range(qt_alunos):
        loadBarr(_, qt_alunos-1)
        adicionou = adicionar_professor()
        if adicionou:
            sucessos += 1
        else:
            erros += 1
    print(f'{sucessos} alunos adicionados. {erros} alunos não adicionados.')


