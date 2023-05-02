from django.contrib import admin
from .models import Autor

class AutorAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'cpf',
        'nacionalidade',
    ]

admin.site.register(Autor, AutorAdmin)
