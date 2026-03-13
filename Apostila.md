Programando em PYTHON - DJANGO

Desativar o Ambiente Virtual: deactivate (Desativa o ambiente virtual atual).
Criar um Novo Ambiente Virtual: python -m venv venv (Cria um novo ambiente virtual chamado .venv).
Ativar o Ambiente Virtual:
Para Windows: .venv\Scripts\activate

Instalar o Django:
pip install django (Instala o Django no ambiente virtual).

Gerar um Arquivo de Dependências:
pip freeze > requirements.txt

Criar um Novo Projeto Django:
django-admin startproject hello-django: Inicializa um novo projeto Django chamado "hello-django".

Executar o Servidor de Desenvolvimento:
python manage.py runserver: Inicia o servidor de desenvolvimento do Django.

Esses comandos são fundamentais para a configuração e execução de projetos Django, e são especialmente úteis para iniciantes que estão aprendendo a trabalhar com essa tecnologia.

Projeto Django:
é a estrutura principal que contém as configurações globais
App Django:
é um módulo que executa uma função específica, como gerenciar tarefas ou usuários.

Instalação de Apps: É crucial incluir novos aplicativos na lista INSTALLED_APPS, pois, se não estiverem listados, o Django não os reconhecerá.

Banco de Dados: O Django utiliza o SQLite 3 por padrão, ideal para testes e desenvolvimento. Futuramente, será integrado o PostgreSQL, um banco de dados relacional.

Configurações de Idioma e Fuso Horário: É importante definir o código de linguagem e o fuso horário, sugerindo o uso de "pt-BR" e "America/Sao_Paulo".

Templates: O settings.py também configura a localização dos templates HTML. O professor mencionou que, nas próximas aulas, será abordada a integração com React e React TypeScript.

Caminhos e Diretórios: O BASE_DIR serve como referência para definir os caminhos dos diretórios do projeto, facilitando a organização.

1. Padrão MTV (Model, Template, View):
   Model: Interage com o banco de dados, realizando consultas e manipulações.
   Template: Interface com o usuário.
   View: Contém a lógica do projeto e conecta Models e Templates.
   ORM (Object Relational Mapping): Facilita a interação entre Models e o banco de dados, permitindo o uso de classes em vez de SQL puro.

2. Criação da Tabela "tarefa":
   Colunas da tabela:
   Título: models.CharField(max_length=100) - Permite até 100 caracteres.
   Descrição: models.TextField(blank=True) - Campo de texto opcional.
   Finalizado: models.BooleanField(default=False) - Indica se a tarefa está finalizada (padrão: não finalizada).
   Criado em: models.DateTimeField(auto_now_add=True) - Armazena a data de criação automaticamente.

3. Processo de Migrações:
   Gerar migração: python manage.py makemigrations - Cria um arquivo com as instruções para criar a tabela.
   Executar migração: python manage.py migrate - Cria a tabela no banco de dados.

   Os principais tópicos abordados foram:

Criação de um Super-Usuário: Aprendemos a criar um super-usuário através do terminal, utilizando o comando python manage.py createsuperuser, onde inserimos um e-mail e uma senha.

Acesso ao Django Admin: Após iniciar o servidor com python manage.py runserver, acessamos a interface administrativa pelo navegador em localhost:8000/admin, onde inserimos as credenciais do super-usuário.

Registro de Modelos: Vimos como registrar o modelo "tarefa" no Django Admin. No arquivo admin.py, importamos o modelo e utilizamos admin.site.register(Tarefa) para torná-lo disponível na interface.

Gerenciamento de Tarefas: Aprendemos a adicionar, editar e visualizar tarefas diretamente no Django Admin. A interface permite criar novas tarefas e listar as existentes de forma simples.

Personalização da Listagem: A aula também abordou como personalizar a tabela de listagem no Django Admin. Utilizando admin.register(Tarefa) e criando uma classe de configuração, podemos definir quais colunas exibir (como título e status de finalização) e adicionar um campo de busca.

Funcionalidades Avançadas: O Django Admin permite filtrar tarefas por status e realizar buscas rápidas, facilitando a administração dos dados.

Os principais métodos HTTP discutidos foram:

GET: Utilizado para buscar dados. Por exemplo, ao acessar uma página ou listar registros, o método GET é empregado. Ele não altera dados, apenas exibe informações.

POST: Usado para enviar dados e criar novos registros. O professor deu o exemplo de criar uma nova tarefa, onde, ao clicar em salvar, uma requisição POST é feita.

PUT: Serve para atualizar todos os campos de um registro. O professor destacou que, ao usar o PUT, é necessário enviar todos os campos, mesmo aqueles que não foram alterados, para evitar que sejam apagados ou deixados como nulos.

PATCH: Utilizado para atualizar apenas parte de um registro. Isso permite que o usuário envie apenas os campos que foram alterados.

DELETE: Remove um registro do banco de dados.

Nesta aula, aprendemos a criar uma funcionalidade para que usuários comuns possam adicionar novas tarefas em um sistema de gerenciamento de tarefas, sem precisar acessar o Django Admin. O fluxo da aula foi o seguinte:

Criação da View: Implementamos uma função chamada novaTarefa que verifica se a requisição é do tipo POST. Se for, ela extrai os dados do título e descrição da tarefa do formulário, cria uma nova tarefa no banco de dados e redireciona o usuário para a página de listagem de tarefas. Se a requisição não for POST, a função renderiza o template do formulário para criar uma nova tarefa.

Configuração da URL: Adicionamos uma nova URL para acessar a função novaTarefa, garantindo que ela esteja acessível através do navegador.

Criação do Formulário: No template nova.html, criamos um formulário que inclui campos para o título e a descrição da tarefa. Também incluímos um token CSRF para segurança, que é necessário para requisições POST no Django.

Navegação: Adicionamos um link na página de listagem de tarefas para que os usuários possam acessar facilmente a página de criação de novas tarefas.

Testes: Por fim, testamos a funcionalidade criando novas tarefas e verificando se elas apareciam corretamente na lista.

A aula enfatizou a importância de manter a segurança nas requisições e a organização do código, além de preparar o terreno para as próximas aulas, onde abordaremos a edição e remoção de tarefas.

Os principais pontos discutidos foram:

Edição de Tarefas:

A view de edição utiliza o método GET para buscar a tarefa pelo ID. Se a tarefa não existir, retorna um erro 404.
Se a requisição for do tipo POST, as informações da tarefa são atualizadas no banco de dados, incluindo o campo "finalizado", que é um checkbox.
Após a edição, o usuário é redirecionado para a página de listagem de tarefas.
Criação da View e Template:

O professor demonstrou como criar a view editar_tarefa e o template editar.html, aproveitando a estrutura do formulário de criação, mas adicionando o valor atual das tarefas nos campos de título e descrição.
Exclusão de Tarefas:

Foi criada uma nova view deletar_tarefa, que também utiliza o ID da tarefa para realizar a exclusão.
O redirecionamento após a exclusão leva o usuário de volta à listagem de tarefas.
Atualização do Template de Listagem:

O professor mostrou como adicionar botões de editar e excluir nas tarefas listadas, utilizando formulários para a exclusão e links para a edição.
Testes Práticos:

Ao final, o professor fez testes práticos, editando e excluindo tarefas, demonstrando que as funcionalidades estavam funcionando corretamente.
A aula concluiu o módulo, preparando os alunos para o próximo, que abordará modelos e a integração com bancos de dados relacionais, especificamente o PostgreSQL.
