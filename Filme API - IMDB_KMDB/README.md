<h1 align="center">
Filme API - IMDB/KMDB
</h1>

## 💻 Projeto

o Filme API - IMDB/KMDB é uma aplicação de gerenciamento de filmes inspirada no IMDB, com autenticação de usuários.

A principal funcionalidade da API é permitir adicionar filmes, criar categorias e definir características para associar a cada filme. Essas tarefas de criação são restritas apenas a superusuários.

Além disso, os críticos têm o privilégio de adicionar avaliações aos filmes. Ao registrar no banco de dados, é essencial inserir as informações corretas para que as avaliações sejam válidas.

A API suporta operações de CRUD (criar, recuperar, atualizar e deletar) e gerencia relacionamentos 1-N e N-N.

## 🔨 Implementações:

- [x] CR User.
- [x] CRUD Movies.
- [x] CRUD Reviews.

## ✨ Tecnologias:

- [x] Django.
- [x] Django Rest Framework.
- [x] Authentication Routes.

# Instruções:
 .
### Crie o ambiente virtual:
```
python -m venv venv.
```
### Ative o venv:
```bash
# linux: 

source venv/bin/activate

```

```bash
# windows: 

.\vevn\Scripts\activate

```

### Instale as dependências :
```
pip install -r requirements.txt
```
### Execute as migrações:
```
./manage.py migrate
```
### Rode a aplicação:
```
./manage.py runserver
```


Essa API é totalmente implementada em Python usando o Django Rest Framework.