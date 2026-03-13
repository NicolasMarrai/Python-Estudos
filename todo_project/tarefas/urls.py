from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarTarefas, name='listarTarefas'),
    path('nova/', views.novaTarefa, name='novaTarefa'),  # URL para criar nova tarefa
]