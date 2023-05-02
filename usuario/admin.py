from django.contrib import admin
from .models import Aluno, Professor, Funcionario

class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        'matricula',
        'nome',
        'cod_curso',
        'ingresso',
    ]

class ProfessorAdmin(admin.ModelAdmin):
    list_display = [
        'siape',
        'nome',
        'regime',
        'cod_curso',
        'contratacao',
    ]

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = [
        'matricula',
        'nome',
    ]

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)