from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.index, name='index'),
    path('login-page/', views.loginPage, name='loginPage'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('biblioteca-aluno/', views.bibliotecaAluno, name='biblioteca-aluno'),
    path('biblioteca-professor/', views.bibliotecaProfessor , name='biblioteca-professor'),
    path('biblioteca-funcionario/', views.bibliotecaFuncionario, name='biblioteca-funcionario'),
    path('biblioteca-admin/', views.bibliotecaAdmin, name='biblioteca-admin'),
]