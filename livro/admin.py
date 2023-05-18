from django.contrib import admin
from .models import Livro, Categoria, Autor

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

admin.site.register(Livro, LivroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
