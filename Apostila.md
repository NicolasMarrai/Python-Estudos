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
