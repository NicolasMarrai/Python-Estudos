from django.shortcuts import render, redirect
from .models import Nota
from django.shortcuts import get_object_or_404


def listar_notas(request):

    notas = Nota.objects.all()

    return render(request, 'notas/listar.html', {'notas': notas})

def nova_nota(request):
    if request.method == 'POST':
        titulo = request.POST["titulo"]
        conteudo = request.POST["conteudo"]
        importante = request.POST.get("importante") == "on"

        Nota.objects.create(
            titulo=titulo,
            conteudo=conteudo,
            importante=importante
        )
        return redirect('listar_notas')
    
    return render(request, 'notas/nova.html')

def editar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    if request.method =='POST':
        nota.titulo = request.POST["titulo"]
        nota.conteudo = request.POST["conteudo"]
        nota.importante = request.POST.get("importante") == "on"
        nota.save()
        return redirect('listar_notas')
    return render(request, 'notas/editar.html', {'nota': nota})

def deletar_nota(request, nota_id):

    nota = get_object_or_404(Nota, id=nota_id)

    if request.method == "POST":
        nota.delete()
        return redirect("listar_notas")

    return render(request, "notas/deletar.html", {"nota": nota})

