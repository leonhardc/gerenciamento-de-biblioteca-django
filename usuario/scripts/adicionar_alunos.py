# from usuario.models import Aluno
# from django.contrib.auth.models import User
from faker import Faker
import random
import string
import re

fake = Faker('pt_BR')


def gerar_senha(tamanho=8):
    # gerar uma senha aleatoria de 8 digitos
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def adicionar_usuario():
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
    email = name_list[0] + "_" + name_list[1] + "@email.com"
    senha = gerar_senha()
    # Criando usuário no django
    usuario_existe = User.objects.filter(username=username).exists()
    if not usuario_existe:
        # Salvando usuário e senha em um arquivo
        nome_arquivo = 'alunos.txt'
        line = f"Usuario: {username} / Senha: {senha}"
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

def adicionar_aluno():
    # Adicionar um aluno na base de dados
    pass
    
def main():
    adicionados = 0
    nao_adicionados = 0
    for _ in range(30):
        usuario = adicionar_usuario()
        if usuario:
            print(usuario, ': Adicionado com sucesso!')
            adicionados += 1
        else:
            print("O usuário que você tentou adicionar já existe na base de dados")
            nao_adicionados += 1
    print(f'{adicionados} usuários adicionados com sucesso, {nao_adicionados} falhas.')

    
if __name__ == '__main__':
    from pprint import pprint
    for _ in range(50):
        endereco = gerar_endereco_brasileiro()
        endereco_str = f"rua: {endereco['rua']}\nnumero: {endereco['numero']}\nbairro: {endereco['bairro']}\ncep: {endereco['cep']}\ncidade: {endereco['cidade']}\nestado: {endereco['estado']}"
        print('\n')
        print(
            endereco_str
        )
