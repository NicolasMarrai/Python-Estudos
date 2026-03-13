from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_notas, name='listar_notas'),
    path('nova/', views.nova_nota, name='nova_nota'),
    path('editar/<int:nota_id>/', views.editar_nota, name='editar_nota'),
    path('deletar/<int:nota_id>/', views.deletar_nota, name='deletar_nota'),
]
