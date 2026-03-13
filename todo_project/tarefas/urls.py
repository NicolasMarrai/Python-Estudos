from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarTarefas, name='listarTarefas'),
    path('nova/', views.novaTarefa, name='novaTarefa'),  # URL para criar nova tarefa
    path('editar/<int:tarefa_id>/', views.editarTarefa, name='editarTarefa'),
    path('deletar/<int:tarefa_id>/', views.deletarTarefa, name='deletarTarefa'),
]