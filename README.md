# REST API Django + OAuth2 + Deploy Heroku
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![Badge](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Badge](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
![Badge](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)


Este projeto consiste em criar um sistema de crud para registros de tarefas utilizando arquitetura rest e sistema de autenticação com OAuth2. Frontend desenvolvido utilizando bootstrap, html, css e javascript.

### Deploy Heroku

https://django-ouath.herokuapp.com/

## Instalação

        git clone https://github.com/andre-bandeli/api-rest-django.git
        
 Crie um ambiente de desenvolvimento com a venv do python com o comando
        
        python3 -m venv [NOME VENV]
        cd venv/ source bin/activate
        
 Caminhe até a pasta rest, onde encontra-se o arquivo 'requirements.txt' e execute o comando
  
        pip install -r requirements.txt
      
 Faça as migrações necessárias com os comandos
     
        python3 manage.py makemigrations && python3 manage.py migrate
        python3 manage.py createsuperuser
        python3 manage.py runserver


### Testes Postman

Objeto JSON

    {
        "nome": "Realizar matrícula",
        "active" : True
    }

Criar novo objeto:

    POST: localhost:8080/create

consultar todos os objetos:

    GET: localhost:8080/list

Deletar objeto por Id:

    DELETE: localhost:8080/delete/{id}
    

### Ferramentas utilizadas

- Django
- Python
- OAtuh2
- JavaScript
- css
- html5


## Rest API

API REST, também chamada de API RESTful, é uma interface de programação de aplicações (API ou API web) que está em conformidade com as restrições do estilo de arquitetura REST, permitindo a interação com serviços web RESTful.[https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api]

- Ter uma arquitetura cliente/servidor formada por clientes, servidores e recursos, com solicitações gerenciadas por HTTP.
- Estabelecer uma comunicação stateless entre cliente e servidor.
- Armazenar dados em cache para otimizar as interações entre cliente e servidor.
- Ter uma interface uniforme entre os componentes para que as informações sejam transferidas em um formato padronizado.
- Sistema em camadas que organiza os tipos de servidores envolvidos na recuperação das informações solicitadas em hierarquias que o cliente não pode ver.
- Possibilitar código sob demanda (opcional): a capacidade de enviar um código executável do servidor para o cliente quando solicitado


![Captura de tela de 2022-05-20 09-09-44_Easy-Resize com](https://user-images.githubusercontent.com/87938869/169526031-db155c5d-4af0-4e0b-a425-f0df1421b963.jpg)
![Captura de tela de 2022-05-20 09-12-37_Easy-Resize com](https://user-images.githubusercontent.com/87938869/169526646-ae052b8a-d0a6-4406-acf8-5c3d42f68c0d.jpg)
![Captura de tela de 2022-05-20 09-10-07_Easy-Resize com](https://user-images.githubusercontent.com/87938869/169526230-b7b5354a-fd33-47d8-b796-fe46e349e11e.jpg)
