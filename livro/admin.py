from django.contrib import admin
from .models import Livro, Categoria, Autor, Reserva, Emprestimo

class LivroAdmin(admin.ModelAdmin):
    list_display = [
        'isbn',
        'titulo',
        'qt_copias',
    ]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'cod_categoria',
        'nome_categoria',
        'desc_categoria',
    ]

class AutorAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'cpf',
        'nacionalidade',
    ]

class ReservaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'usuario',
        'livro',
        'data_reserva'
    ]

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'usuario',
        'livro',
        'data_emprestimo',
        'data_devolucao',
    ]

admin.site.register(Livro, LivroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
