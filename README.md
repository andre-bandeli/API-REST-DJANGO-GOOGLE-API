# Rest API Django + OAuth2 + Deploy Heroku
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)


## Instalação

  - Clone o repositório com o comando: git clone
  - Crie um ambiente de desenvolvimento com a venv do python com o comando: python3 -m venv [NOME VENV]
  - Ative a venv com o comando: cd venv/ source bin/activate
  - Caminhe até a pasta rest, onde encontra-se o arquivo 'requirements.txt' e execute o comando: pip install -r requirements.txt
  - Faça as migrações necessárias com os comandos: python3 manage.py makemigrations && python3 manage.py migrate
  - Crie um novo super usuário com o comando: python3 manage.py createsuperuser
  - Rode o servidor local com o comando: python3 manage.py runserver


## Rest API

API REST, também chamada de API RESTful, é uma interface de programação de aplicações (API ou API web) que está em conformidade com as restrições do estilo de arquitetura REST, permitindo a interação com serviços web RESTful.[https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api]

- Ter uma arquitetura cliente/servidor formada por clientes, servidores e recursos, com solicitações gerenciadas por HTTP.
- Estabelecer uma comunicação stateless entre cliente e servidor. Isso significa que nenhuma informação do cliente é armazenada entre solicitações GET e toda as solicitações são separadas e desconectadas.
- Armazenar dados em cache para otimizar as interações entre cliente e servidor.
- Ter uma interface uniforme entre os componentes para que as informações sejam transferidas em um formato padronizado. Para tanto, é necessário que:
os recursos solicitados sejam identificáveis e estejam separados das representações enviadas ao cliente;
  - Os recursos possam ser manipulados pelo cliente por meio da representação recebida com informações suficientes para tais ações;
  - as mensagens autodescritivas retornadas ao cliente contenham informações suficientes para descrever como processá-las;
  - hipertexto e hipermídia estão disponíveis. Isso significa que após acessar um recurso, o cliente pode usar hiperlinks para encontrar as demais ações disponíveis para ele no momento.
- Ter um sistema em camadas que organiza os tipos de servidores (responsáveis pela segurança, pelo carregamento de carga e assim por diante) envolvidos na recuperação das informações solicitadas em hierarquias que o cliente não pode ver.
- Possibilitar código sob demanda (opcional): a capacidade de enviar um código executável do servidor para o cliente quando solicitado para ampliar a funcionalidade disponível ao cliente. 

## OAuth 2

OAuth 2 é um protocolo de autorização que permite que uma aplicação se autentique em outra. Para que isso aconteça, uma aplicação pede permissão de acesso para um usuário, sem que para isso ela tenha acesso a alguma senha dele. O usuário pode conceder ou não o acesso à aplicação. Depois da permissão ser aceita, caso o usuário precise alterar a senha de acesso, a permissão continuará válida para a aplicação e, caso necessário, a permissão dada à aplicação pode ser revogada a qualquer momento também.

Provavelmente você já clicou em algum botão escrito “Logar com sua conta do Google” ou “Logar com sua conta do Facebook” quando você está em alguma outra aplicação, para evitar de ter que fazer na mão algum cadastro. Neste caso, você está dando a autorização de uma aplicação terceira a usar os recursos da sua aplicação, neste caso o Google ou o Facebook. Essas aplicações têm acesso limitado às informações de usuários através do protocolo HTTP. OAuth 2 é utilizado nos mais diversos tipos de autenticação, como em telas de login e na autenticação de APIs (Application Programming Interface). https://www.treinaweb.com.br/blog/o-que-e-oauth-2
