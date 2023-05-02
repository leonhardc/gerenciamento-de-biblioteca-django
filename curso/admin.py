from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = [
        'cod_curso',
        'nome_curso'
    ]

admin.site.register(Curso, CursoAdmin)
