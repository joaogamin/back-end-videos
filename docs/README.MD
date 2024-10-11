# Projeto Back-end

----

## Descrição

Esta é a solução back-end do desafio, uma API para gerenciar URLs de vídeos do YouTube. A API permite
inserir, listar, alterar e deletar vídeos. Foi desenvolvida utilizando **Python** com o framework **Flask** e está
conectada a
um banco de dados **PostgreSQL** para armazenar as URLs. A documentação da API está disponível via **Swagger**,
facilitando o
uso e a integração. Para o deploy da API foi utilizada a plataforma **Render**.

---

## Funcionalidades

- **Inserir vídeo**: Permite adicionar vídeos do YouTube através de uma URL, capturando o ID, título e duração.
- **Listar vídeos**: Retorna uma lista de vídeos previamente armazenados.
- **Deletar vídeo**: Permite ao usuário remover vídeos (URLs) da lista.
- **Atualizar vídeo**: Permite atualizar informações de um vídeo existente, substituindo a URL.
- **Documentação via Swagger**: A API conta com uma documentação detalhada no Swagger para facilitar o uso e testes.

---

## Tecnologias Utilizadas

- **Flask**: Framework web utilizado para o desenvolvimento da API.
- **SQLAlchemy**: ORM utilizado para a interação com o banco de dados PostgreSQL.
- **PostgreSQL**: Banco de dados utilizado para armazenar as URLs dos vídeos.
- **Render**: Plataforma utilizada para deploy da API.
- **Swagger**: Utilizado para gerar a documentação da API e facilitar os testes.

----

## Requisitos para rodar a aplicação localmente

- **Python** (v3.8 ou superior)
- **Pip** para gerenciamento de dependências
- **PostgreSQL** **Docker** para o banco de dados

-------

## Instalação e Configuração

1. Clone o repositório do projeto:

   ```bash
   git clone https://github.com/joaogamin/back-end-videos.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd back-end-videos
   ```

3. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente no arquivo .env para conexão com o banco de dados PostgreSQL e outras
   configurações:
   back-end:

   ```dotenv
    SECRET_KEY="Chave Aleatória para criptografia"
    ```
    ```dotenv
    SQLALCHEMY_DATABASE_URI="postgresql+pg8000://usuario:
    senha@endereço-do-banco-de-dados-postegres/nome-do-banco-de-dados"
    ```
    ```dotenv
    GOOGLE_API_KEY="Chave da API do YouTube V3"
    ```

5. Inicie o docker do projeto (opcional):
   ```bash
   docker compose up -d
   ```

6. Inicie o projeto localmente:
   ```bash
   flask run --host-0.0.0.0 --port=3333 --debug
   ```

## Como Usar a Solução

Para rodar o projeto localmente, siga os passos abaixo:

1. Inicie o servidor localmente com o comando:

  ```bash
   flask run --host=0.0.0.0 --port=3333 --debug
  ```

2. Acesse a API via http://localhost:3333 para realizar as operações CRUD de vídeos.:

3. Para visualizar a documentação do Swagger, acesse http://localhost:3333/apidocs. A documentação permite testar as
   rotas diretamente pela interface Swagger.

4. Rotas principais:
    - **GET /videos**: Listar todos os vídeos.
    - **GET /videos/{video_id}**: Receber as informações de um vídeo.
    - **POST /videos**: Inserir um novo vídeo.
    - **PATCH /videos/{video_id}**: Atualizar um vídeo existente.
    - **DELETE /videos/{video_id}**: Deletar um vídeo.

----

## Deploy

O deploy da API é feito na plataforma Render. Acesse o documento de instrução de deploy para seguir
o [passo a passo](./deploy.md).

----

## Bugs ou Observações

- **Chave API do YouTube**: Para inserir vídeos, é necessário configurar corretamente a chave da API do YouTube no
  arquivo ```.env```.

## Sugestões de Melhorias

- **Inserção de vídeos de outros provedores**: Expandir a funcionalidade para suportar vídeos de outras plataformas além
  do YouTube.
- **Autenticação de usuários**: Implementar um sistema de autenticação para que diferentes usuários possam gerenciar
  suas próprias listas de vídeos.
- **Pesquisas**: Implementar uma funcionalidade de busca dentro da lista de vídeos armazenados.
- **Testes**: Implementar testes automatizados (unitários, integração e e2e) para maior consistência e confiabilidade no código.

----
