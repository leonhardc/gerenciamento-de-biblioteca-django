from curso.models import Curso
import os
import sys

# Adicione o diretório raiz do seu projeto Django ao sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Configure as configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteca.settings")
import django
django.setup()

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

# Verifica se já existem cursos no banco de dados
if Curso.objects.exists():
    print("Já existem cursos cadastrados.")
else:
    # Adiciona os cursos no banco de dados
    for codigo, nome in enumerate(cursos, start=1):
        curso = Curso(cod_curso=str(codigo).zfill(3), nome_curso=nome)
        curso.save()

    print("Cursos adicionados com sucesso.")


from curso.models import Curso

