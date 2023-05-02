from django.contrib import admin
from .models import Livro, Categoria

class LivroAdmin(admin.ModelAdmin):
    list_display = [
        'isbn',
        'titulo',
        'qt_copias',
        'autores',
    ]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'cod_categoria',
        'nome_categoria',
        'desc_categoria',
    ]

admin.site.register(Livro, LivroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
