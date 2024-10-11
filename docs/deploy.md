# Guia de Deploy de API Flask na Render

## Pré-requisitos

- API Flask pronta em um repositório no GitHub, GitLab ou Bitbucket.
- Conta criada na plataforma [Render](https://render.com).

---

## Passo 1: Criar uma nova conta ou fazer login

1. Acesse [Render.com](https://render.com).
2. Caso não tenha uma conta, crie uma clicando no botão **Get Started**.
3. Se já possuir uma conta, faça login.

---

## Passo 2: Criar um novo serviço Web

1. No painel da Render, clique em **New** e selecione **Web Service**.
2. Conecte sua conta GitHub, GitLab ou Bitbucket para acessar seus repositórios.
3. Escolha o repositório da sua API Flask.

---

## Passo 3: Configurar o serviço

1. Defina um nome para o seu serviço.
2. Em **Language**, selecione **Python 3**.
3. Em **Build Command**, insira o seguinte comando:

   ```bash
   pip install -r requirements.txt
    ```

4. Em **Start Command**, coloque o comando para rodar sua aplicação Flask.

   ```bash
   flask run --host=0.0.0.0 --port=3333
   ```

---

## Caso não tenha um Banco de Dados PostgresSQL

Você pode criar um banco acessando esse documento: [Deploy Banco De Dados](./deploy-database)

## Passo 4: Configurar variáveis de ambiente

1. Sua API vai precisar de variáveis de ambiente (como chaves de API ou configurações de banco de dados), configure-as
   na
   aba **Environment Variables**.
2. Adicione as seguintes variáveis necessárias para o correto funcionamento da aplicação.
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

    
---

## Passo 5: Iniciar o Deploy

1. Após definir todas as configurações, clique em **Deploy Web Service**.
2. A Render irá iniciar o processo de build e deploy da sua aplicação.
3. Você poderá acompanhar os logs da build em tempo real diretamente no painel.

---

## Passo 6: Verificar o Deploy

1. Quando o deploy estiver concluído, a Render exibirá a URL pública da sua API, algo
   como \`https://sua-api.onrender.com/apidocs \`.
2. Acesse essa URL para testar se sua API está funcionando corretamente.
3. Caso queria acesse o caminho \`/apidocs \`

---

## Passo 7: Deploys Automáticos

1. A cada push que você fizer no repositório conectado, a Render automaticamente irá gerar um novo deploy da sua API.

---

## Considerações Finais

- A Render lida automaticamente com a hospedagem, balanceamento de carga e manutenção de servidores, facilitando o
  processo.
- Sempre que necessário, adicione novas variáveis de ambiente ou ajuste configurações diretamente no painel da Render.
