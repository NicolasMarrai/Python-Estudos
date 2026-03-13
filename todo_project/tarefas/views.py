from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa  # Certifique-se de que o modelo Tarefa está importado

def listarTarefas(request):
    tarefas = Tarefa.objects.all()  # Obtém todas as tarefas
    return render(request, 'tarefas/listar.html', {'tarefas': tarefas})

def novaTarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(titulo=titulo, descricao=descricao, finalizado=False)  # Cria a nova tarefa
        return redirect('listarTarefas')  # Redireciona para a lista de tarefas
    return render(request, 'tarefas/nova.html')  # Renderiza o formulário para criar nova tarefa

def editarTarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.finalizado = 'finalizado' in request.POST
        tarefa.save()
        return redirect('listarTarefas')
    
    return render(request, 'tarefas/editar.html', {'tarefa': tarefa})

def deletarTarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('listarTarefas')