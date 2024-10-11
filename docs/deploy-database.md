# Guia de Criação e Configuração de Banco de Dados PostgreSQL na Render

## Pré-requisitos

- Conta criada na plataforma [Render](https://render.com).
- Aplicação pronta para se conectar a um banco de dados PostgreSQL.

---

## Passo 1: Criar uma nova conta ou fazer login

1. Acesse [Render.com](https://render.com).
2. Caso não tenha uma conta, crie uma clicando no botão **Get Started**.
3. Se já possuir uma conta, faça login.

---

## Passo 2: Criar um banco de dados PostgreSQL

1. No painel da Render, clique em **New** e selecione **PostgreSQL**.

---

## Passo 3: Configurar o banco de dados

1. Dê um nome para o seu banco de dados.

---

## Passo 4: Finalizar a criação do banco de dados

1. Após configurar o banco de dados, clique em **Create Database**.
2. A Render criará o banco de dados e exibirá as credenciais de conexão (Host, Database, User, Password, e Port).
3. Há a opção de utilizar a Internal Database URL caso a aplicação estiver no Render. Apenas garanta de incluir pg8000
   após "postgresql+pg800://usuario:senha@endereço-do-banco/nome-do-banco"

---

