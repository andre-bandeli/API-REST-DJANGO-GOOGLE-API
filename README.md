# Rest API utilizando Django
Sistema de leitura, adição, edição e remoção (CRUD) para app 'to do' + api Google Developers (autenticação Google Gmail) + oauth

Projeto independente open-source desenvolvido em Python 3 com Linux Ubuntu 20.0
.
## Dependências 

- Python - Versão 3.5+
- asgiref==3.4.1
- backports.zoneinfo==0.2.1
- certifi==2021.10.8
- cffi==1.15.0
charset-normalizer==2.0.10
cryptography==36.0.1
defusedxml==0.7.1
Django==4.0.1
django-allauth==0.47.0
idna==3.3
oauthlib==3.1.1
pkg_resources==0.0.0
psycopg2-binary==2.9.3
pycparser==2.21
PyJWT==2.3.0
python3-openid==3.2.0
requests==2.27.1
requests-oauthlib==1.3.0
social-auth-app-django==5.0.0
social-auth-core==4.2.0
sqlparse==0.4.2
urllib3==1.26.8


Instalação:
Instalar as bibliotecas/pacotes (no Linux):
sudo apt install -y libxml2 gcc python3-dev libxml2-dev libxslt1-dev zlib1g-dev python3-pip
sudo apt update
Instalar dependências:
pip install -r requirements.txt
Edite o conteúdo do arquivo djangosige/configs/configs.py

Gere um .env local

python contrib/env_gen.py
Sincronize a base de dados:
python manage.py migrate
Crie um usuário (Administrador do sistema):
python manage.py createsuperuser
Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):
python manage.py runserver
Implementações
Cadastro de produtos, clientes, empresas, fornecedores e transportadoras
Login/Logout
Criação de perfil para cada usuário.
Definição de permissões para usuários.
Criação e geração de PDF para orçamentos e pedidos de compra/venda
Módulo financeiro (Plano de Contas, Fluxo de Caixa e Lançamentos)
Módulo para controle de estoque
Módulo fiscal:
Geração e armazenamento de notas fiscais
Validação do XML de NF-e/NFC-es
Emissão, download, consulta e cancelamento de NF-e/NFC-es (Testar em ambiente de homologação)
Comunicação com SEFAZ (Consulta de cadastro, inutilização de notas, manifestação do destinatário)
Interface simples e em português
Créditos
AdminBSBMaterialDesign
geraldo
jQuery-Mask-Plugin
DataTables
JQuery multiselect
Ajuda
Para relatar bugs ou fazer perguntas utilize o Issues ou via email thiagopena01@gmail.com

Como este é um projeto em desenvolvimento, qualquer feedback será bem-vindo.
