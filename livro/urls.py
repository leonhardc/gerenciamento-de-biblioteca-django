from django.urls import path
from . import views

app_name = 'livro'

urlpatterns = [
    path('livros/', views.lista_livros, name='lista_livros'),
]