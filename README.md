# CryptoSafe

CryptoSafe é um sistema de cofres que oferece proteção, organização e segurança a suas senhas. Com ele, suas informações sensíveis estarão protegidas de forma eficiente e eficaz.

## 💻 Pré-requisitos

Antes de começar, certifique-se de ter instalado o Python 3.9+ e de ter criado uma virtualenv.
* `pip install virtualenv` instalando a biblioteca
* `python -m venv nome-env` criando a virtualenv
* `nome-env/Scripts/Activate.ps1` iniciando a virtualenv

## ⚙️ Instalação 

Primeiramente, para iniciar o projeto, é necessário instalar as dependências do Python e do Django. Para isso, execute o seguinte comando:
```bash
pip install -r requirements.txt
```

Em seguida, execute os seguintes comandos para criar as tabelas no banco de dados:
```bash
1 - python manage.py makemigrations

2 - python manage.py migrate
```

## 🚀 Execução

Para executar o projeto, execute o seguinte comando:
```bash
python manage.py runserver
```

Acesse a página do projeto em `http://localhost:8000/`