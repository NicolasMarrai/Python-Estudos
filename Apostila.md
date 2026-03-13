# Apostila Django: Sistema de Notas (CRUD)

## Objetivo

Neste exercicio, voce vai criar um sistema de notas de estudo com CRUD completo.

Cada nota tera:

- titulo
- conteudo
- importante (True/False)

Voce vai aprender a:

- listar notas (Read)
- criar notas (Create)
- editar notas (Update)
- excluir notas (Delete)
- gerenciar dados no Django Admin

---

## Pre-requisitos

- Python instalado
- VS Code (ou outro editor)
- Terminal aberto na pasta de trabalho

---

## Etapa 1 - Criar a pasta do projeto

```bash
mkdir projeto_notas
cd projeto_notas
```

Para conferir arquivos:

```bash
dir
# ou
ls
```

---

## Etapa 2 - Criar ambiente virtual

```bash
python -m venv venv
```

---

## Etapa 3 - Ativar ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

Se tudo der certo, o terminal mostra algo como:

```text
(venv) C:\projeto_notas>
```

---

## Etapa 4 - Instalar Django

```bash
pip install django
```

---

## Etapa 5 - Salvar dependencias

```bash
pip freeze > requirements.txt
```

---

## Etapa 6 - Criar projeto Django

```bash
django-admin startproject config
cd config
```

Estrutura esperada:

```text
projeto_notas/
|-- venv/
|-- requirements.txt
`-- config/
    |-- manage.py
    `-- config/
        |-- settings.py
        `-- urls.py
```

---

## Etapa 7 - Rodar servidor

```bash
python manage.py runserver
```

Acesse:

- http://127.0.0.1:8000

Para parar o servidor:

```text
CTRL + C
```

---

## Etapa 8 - Criar app notas

```bash
python manage.py startapp notas
```

---

## Etapa 9 - Registrar app no settings

No arquivo [projeto_notas/config/config/settings.py](projeto_notas/config/config/settings.py), adicione no INSTALLED_APPS:

```python
'notas',
```

Exemplo:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notas',
]
```

---

## Etapa 10 - Criar model Nota

No arquivo [projeto_notas/config/notas/models.py](projeto_notas/config/notas/models.py):

```python
from django.db import models


class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    importante = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
```

---

## Etapa 11 - Criar migracoes

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Etapa 12 - Registrar model no Admin

No arquivo [projeto_notas/config/notas/admin.py](projeto_notas/config/notas/admin.py):

```python
from django.contrib import admin
from .models import Nota

admin.site.register(Nota)
```

---

## Etapa 13 - Criar superusuario

```bash
python manage.py createsuperuser
```

Exemplo:

- username: admin
- email: admin@email.com
- password: 123456

---

## Etapa 14 - Testar Admin

```bash
python manage.py runserver
```

Acesse:

- http://127.0.0.1:8000/admin

---

## Etapa 15 - View para listar notas (Read)

No arquivo [projeto_notas/config/notas/views.py](projeto_notas/config/notas/views.py):

```python
from django.shortcuts import render
from .models import Nota


def listar_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/listar.html', {'notas': notas})
```

---

## Etapa 16 - URLs do app

Crie [projeto_notas/config/notas/urls.py](projeto_notas/config/notas/urls.py):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_notas, name='listar_notas'),
]
```

---

## Etapa 17 - Conectar URLs no projeto

No arquivo [projeto_notas/config/config/urls.py](projeto_notas/config/config/urls.py):

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notas.urls')),
]
```

---

## Etapa 18 - Criar pasta de templates

Estrutura:

```text
notas/
`-- templates/
    `-- notas/
        `-- listar.html
```

---

## Etapa 19 - Template de listagem

No arquivo [projeto_notas/config/notas/templates/notas/listar.html](projeto_notas/config/notas/templates/notas/listar.html):

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Lista de Notas</title>
  </head>
  <body>
    <h1>Minhas Notas</h1>

    <ul>
      {% for nota in notas %}
      <li>
        <strong>{{ nota.titulo }}</strong>
        {% if nota.importante %} - ⭐ Importante {% endif %}
        <br />
        {{ nota.conteudo }}
      </li>
      {% empty %}
      <li>Nenhuma nota encontrada.</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

---

## Etapa 20 - Testar listagem

```bash
python manage.py runserver
```

Acesse:

- http://127.0.0.1:8000

---

## Etapa 21 - View para criar nota (Create)

Atualize [projeto_notas/config/notas/views.py](projeto_notas/config/notas/views.py):

```python
from django.shortcuts import render, redirect
from .models import Nota


def listar_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/listar.html', {'notas': notas})


def nova_nota(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        importante = request.POST.get('importante') == 'on'

        Nota.objects.create(
            titulo=titulo,
            conteudo=conteudo,
            importante=importante,
        )
        return redirect('listar_notas')

    return render(request, 'notas/nova.html')
```

---

## Etapa 22 - URL da nova nota

No arquivo [projeto_notas/config/notas/urls.py](projeto_notas/config/notas/urls.py):

```python
urlpatterns = [
    path('', views.listar_notas, name='listar_notas'),
    path('nova/', views.nova_nota, name='nova_nota'),
]
```

---

## Etapa 23 - Template de criacao

Crie [projeto_notas/config/notas/templates/notas/nova.html](projeto_notas/config/notas/templates/notas/nova.html):

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Nova Nota</title>
  </head>
  <body>
    <h1>Criar Nova Nota</h1>

    <form method="POST">
      {% csrf_token %}

      <label>Titulo:</label><br />
      <input type="text" name="titulo" />

      <br /><br />

      <label>Conteudo:</label><br />
      <textarea name="conteudo"></textarea>

      <br /><br />

      <label>
        <input type="checkbox" name="importante" />
        Nota importante
      </label>

      <br /><br />

      <button type="submit">Salvar</button>
    </form>

    <br />
    <a href="/">Voltar para lista</a>
  </body>
</html>
```

---

## Etapa 24 - Botao de criar na listagem

No arquivo [projeto_notas/config/notas/templates/notas/listar.html](projeto_notas/config/notas/templates/notas/listar.html), abaixo do titulo:

```html
<a href="/nova">Criar nova nota</a> <br /><br />
```

---

## Etapa 25 - Testar Create

Fluxo esperado:

1. Lista de notas
2. Criar nova nota
3. Salvar
4. Voltar para lista

---

## Etapa 26 - View para editar nota (Update)

Atualize [projeto_notas/config/notas/views.py](projeto_notas/config/notas/views.py):

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota


def editar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)

    if request.method == 'POST':
        nota.titulo = request.POST['titulo']
        nota.conteudo = request.POST['conteudo']
        nota.importante = request.POST.get('importante') == 'on'
        nota.save()
        return redirect('listar_notas')

    return render(request, 'notas/editar.html', {'nota': nota})
```

---

## Etapa 27 - URL da edicao

No arquivo [projeto_notas/config/notas/urls.py](projeto_notas/config/notas/urls.py):

```python
urlpatterns = [
    path('', views.listar_notas, name='listar_notas'),
    path('nova/', views.nova_nota, name='nova_nota'),
    path('editar/<int:nota_id>/', views.editar_nota, name='editar_nota'),
]
```

---

## Etapa 28 - Template de edicao

Crie [projeto_notas/config/notas/templates/notas/editar.html](projeto_notas/config/notas/templates/notas/editar.html):

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Editar Nota</title>
  </head>
  <body>
    <h1>Editar Nota</h1>

    <form method="POST">
      {% csrf_token %}

      <label>Titulo:</label><br />
      <input type="text" name="titulo" value="{{ nota.titulo }}" />

      <br /><br />

      <label>Conteudo:</label><br />
      <textarea name="conteudo">{{ nota.conteudo }}</textarea>

      <br /><br />

      <label>
        <input
          type="checkbox"
          name="importante"
          {%
          if
          nota.importante
          %}checked{%
          endif
          %}
        />
        Nota importante
      </label>

      <br /><br />

      <button type="submit">Salvar alteracoes</button>
    </form>

    <br />
    <a href="/">Voltar</a>
  </body>
</html>
```

---

## Etapa 29 - Botao Editar na listagem

No loop de [projeto_notas/config/notas/templates/notas/listar.html](projeto_notas/config/notas/templates/notas/listar.html):

```html
<a href="/editar/{{ nota.id }}">Editar</a>
```

---

## Etapa 30 - Testar Update

Fluxo esperado:

1. Lista
2. Editar
3. Alterar dados
4. Salvar
5. Voltar para lista

---

## Etapa 31 - View para excluir nota (Delete)

Atualize [projeto_notas/config/notas/views.py](projeto_notas/config/notas/views.py):

```python
def deletar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)

    if request.method == 'POST':
        nota.delete()
        return redirect('listar_notas')

    return render(request, 'notas/deletar.html', {'nota': nota})
```

---

## Etapa 32 - URL de exclusao

No arquivo [projeto_notas/config/notas/urls.py](projeto_notas/config/notas/urls.py):

```python
urlpatterns = [
    path('', views.listar_notas, name='listar_notas'),
    path('nova/', views.nova_nota, name='nova_nota'),
    path('editar/<int:nota_id>/', views.editar_nota, name='editar_nota'),
    path('deletar/<int:nota_id>/', views.deletar_nota, name='deletar_nota'),
]
```

---

## Etapa 33 - Template de confirmacao de exclusao

Crie [projeto_notas/config/notas/templates/notas/deletar.html](projeto_notas/config/notas/templates/notas/deletar.html):

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Deletar Nota</title>
  </head>
  <body>
    <h1>Excluir Nota</h1>

    <p>Tem certeza que deseja excluir a nota:</p>
    <strong>{{ nota.titulo }}</strong>

    <form method="POST">
      {% csrf_token %}
      <br /><br />
      <button type="submit">Confirmar exclusao</button>
    </form>

    <br />
    <a href="/">Cancelar</a>
  </body>
</html>
```

---

## Etapa 34 - Botao Excluir na listagem

No loop de [projeto_notas/config/notas/templates/notas/listar.html](projeto_notas/config/notas/templates/notas/listar.html):

```html
<a href="/deletar/{{ nota.id }}">Excluir</a>
```

---

## Etapa 35 - Testar CRUD completo

Fluxo final:

1. Criar nota
2. Listar notas
3. Editar nota
4. Excluir nota

---

## Resumo do que voce praticou

- models
- migrations
- Django admin
- views
- urls
- templates
- forms
- GET e POST
- ORM
- CRUD completo

Esse conjunto e a base de praticamente qualquer sistema web com Django.

---

## Observacao importante

Se aparecer erro de template nao encontrado em /deletar/<id>/, confirme se o arquivo existe com o nome exato:

- [projeto_notas/config/notas/templates/notas/deletar.html](projeto_notas/config/notas/templates/notas/deletar.html)

No seu projeto, existe [projeto_notas/config/notas/templates/notas/deletra.html](projeto_notas/config/notas/templates/notas/deletra.html), que esta com nome diferente. Renomeie para deletar.html para resolver.
