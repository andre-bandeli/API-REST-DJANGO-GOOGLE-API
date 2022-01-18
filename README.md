## Rest API utilizando Django ![Badge](https://img.shields.io/badge/rest-api-%237159c1?style=for-the-badge&logo=ghost)
#### Sistema de leitura, adição, edição e remoção (CRUD) para app 'to do' + api Google Developers (autenticação Google Gmail) + oauth

Projeto independente open-source desenvolvido em Python 3 com Linux Ubuntu 20.0
.
### Dependências 

- Python - Versão 3.5+
- Django==4.0.1
- django-allauth==0.47.0
- oauthlib==3.1.1
- psycopg2-binary==2.9.3
- requests==2.27.1
- requests-oauthlib==1.3.0
- social-auth-app-django==5.0.0
- social-auth-core==4.2.0


### Instalação:

- pip install -r requirements.txt
é considerado boa prática ativar uma virtual env para gerencias as dependências necessárias.

### Banco de dados:

- python3 manage.py makemigrations
- python3 manage.py migrate

obs: o app está utilizando o postgres como banco de dados.
É necessário que seja configurado os padrões de acesso ao banco no arquivo settings.


### Crie um usuário (Administrador do sistema):

- python manage.py createsuperuser

### Teste a instalação 
carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):
- python manage.py runserver


### Implementações

#### Gestão de tarefas (to do) com criação, remoção, update e deleção (CRUD) integrada ao PostgreSQL.

Login/Logout utilizando oauth | Definição de permissões para usuários | Frontend: Bootstrap, css e html-5


### Como este é um projeto em desenvolvimento, qualquer feedback será bem-vindo.
