from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.index, name='index'),
]