# Apostila do Projeto Django de Tarefas

## 1. Objetivo do que eu construí

Neste projeto, eu desenvolvi uma aplicação web simples de lista de tarefas (to-do list) com Django, com as operações de:

- criar tarefa
- listar tarefas
- editar tarefa
- deletar tarefa
- marcar tarefa como finalizada

Além de implementar o CRUD, eu também aprendi a estruturar o projeto, trabalhar com templates HTML, configurar ambiente virtual, usar migrações e corrigir erros comuns de desenvolvimento.

## 2. Estrutura do projeto

Eu organizei o projeto principal em uma pasta chamada todo_project, contendo:

- manage.py (comandos do Django)
- pasta do projeto Django (configurações globais)
- app tarefas (regra de negócio e telas de tarefas)
- db.sqlite3 (banco de dados local)
- venv local do projeto

Conceitos importantes:

- Projeto Django: contém configurações globais (settings, urls, wsgi, asgi).
- App Django: módulo com uma responsabilidade específica. Neste caso, o app tarefas cuida de tudo relacionado a tarefas.

## 3. Ambiente virtual e instalação

### 3.1. Criação e ativação do ambiente

No Windows, o processo correto é:

```powershell
python -m venv venv
venv\Scripts\activate
```

Para sair do ambiente virtual:

```powershell
deactivate
```

### 3.2. Instalação do Django

Com o ambiente virtual ativo:

```powershell
pip install django
```

Para salvar dependências:

```powershell
pip freeze > requirements.txt
```

### 3.3. Aprendizado importante sobre ambiente

Durante o desenvolvimento, eu encontrei um problema de ambiente Python por ter mais de um interpretador disponível no Windows.

- Um interpretador não tinha o Django instalado.
- O projeto estava funcionando com o venv dentro da pasta do projeto.

Lição prática:

- sempre executar comandos do Django com o Python do venv correto do projeto
- evitar misturar python, python3 e outros ambientes sem confirmar qual está ativo

## 4. Configuração inicial do Django

Com o projeto criado, os comandos principais usados foram:

```powershell
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py check
```

O que cada comando faz:

- runserver: sobe o servidor local.
- makemigrations: gera arquivos de migração com mudanças dos models.
- migrate: aplica as migrações no banco.
- check: valida configurações e integridade do projeto.

## 5. Modelagem da aplicação

No app tarefas, foi criado o model Tarefa com os campos:

- titulo: texto curto obrigatório (CharField)
- descricao: texto livre opcional (TextField com blank=True)
- finalizado: status booleano (BooleanField)
- criado_em: data/hora automática de criação (DateTimeField auto_now_add=True)

Com isso, o Django ORM passou a mapear essa classe para uma tabela no SQLite automaticamente após as migrações.

## 6. Painel administrativo

Para administração inicial dos dados, o fluxo foi:

1. criar superusuário
2. acessar /admin
3. registrar o model Tarefa no admin.py
4. criar e visualizar tarefas pelo painel

Também foi entendido que o Django Admin permite filtros, busca e customização da listagem.

## 7. Implementação do CRUD no app tarefas

### 7.1. Listagem

- view: listarTarefas
- objetivo: buscar todas as tarefas no banco e renderizar o template de listagem

### 7.2. Criação

- view: novaTarefa
- método GET: mostra formulário
- método POST: recebe titulo e descricao, cria no banco e redireciona

### 7.3. Edição

- view: editarTarefa
- busca tarefa por ID com get_object_or_404
- método GET: abre formulário preenchido
- método POST: atualiza dados da tarefa e redireciona

### 7.4. Exclusão

- view: deletarTarefa
- remove a tarefa pelo ID e redireciona para a listagem

## 8. Templates HTML criados

No app tarefas, eu trabalhei com:

- listar.html
- nova.html
- editar.html

Pontos aplicados nos formulários:

- uso de method="post"
- inclusão de token CSRF ({% csrf_token %})
- preenchimento de valores existentes na edição
- link de navegação para voltar à listagem

## 9. Métodos HTTP usados na prática

No projeto, os principais foram:

- GET: abrir páginas e listar dados
- POST: enviar formulário para criar ou atualizar

Também estudei conceitualmente:

- PUT: atualização completa
- PATCH: atualização parcial
- DELETE: remoção

## 10. Erros reais que aconteceram e como corrigi

Esta foi uma parte importante do aprendizado prático.

### 10.1. Erro no template: endif inválido

Problema:

- TemplateSyntaxError informando tag endif inválida no editar.html

Causa:

- sintaxe da tag if/endif fora do padrão do template engine do Django

Correção:

- padronização para {% if tarefa.finalizado %} ... {% endif %}

### 10.2. Erro no formulário: campo titulo não era enviado

Problema:

- edição não enviava o título corretamente

Causa:

- atributo digitado errado no input (nam em vez de name)

Correção:

- ajustar para name="titulo"

### 10.3. Erro de validação do BooleanField

Problema:

- ValidationError: valor on deve ser True ou False

Causa:

- checkbox enviado como string on e salvo diretamente no campo booleano

Correção aplicada na view:

```python
tarefa.finalizado = 'finalizado' in request.POST
```

Por que funciona:

- se checkbox estiver marcado, o campo finalizado vem no POST
- se estiver desmarcado, o campo não vem
- resultado final vira True ou False corretamente

## 11. Fluxo completo de uso da aplicação

1. iniciar servidor com runserver
2. abrir listagem de tarefas
3. criar nova tarefa pelo formulário
4. editar título, descrição e status de finalização
5. excluir tarefa quando necessário

Esse fluxo confirma o CRUD funcionando de ponta a ponta.

## 12. O que eu aprendi com este projeto

- estrutura base de um projeto Django
- diferença entre projeto e app
- padrão MTV e papel de cada camada
- uso de ORM para persistência em SQLite
- criação de views baseadas em função
- integração entre URLs, views, templates e models
- tratamento de erros reais de template, formulário e tipo de dado
- importância de usar o ambiente virtual correto no Windows

## 13. Próximos passos sugeridos

- refinar interface visual com CSS
- criar validações mais completas de formulário
- adicionar testes automatizados
- evoluir banco de SQLite para PostgreSQL
- futuramente expor API para integração com front-end React
