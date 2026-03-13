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
