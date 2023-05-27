from django.urls import path
from . import views
import livro.views

app_name = 'usuario'

urlpatterns = [
    path('', views.index, name='index'),
    path('login-page/', views.loginPage, name='loginPage'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('biblioteca-aluno/', views.bibliotecaAluno, name='biblioteca-aluno'),
    path('biblioteca-aluno/livros/', livro.views.lista_livros, name='lista_livros'),
    
    path('biblioteca-professor/', views.bibliotecaProfessor , name='biblioteca-professor'),
    path('biblioteca-funcionario/', views.bibliotecaFuncionario, name='biblioteca-funcionario'),
    path('biblioteca-admin/', views.bibliotecaAdmin, name='biblioteca-admin'),
]