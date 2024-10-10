# Projeto Back-end


#### Requisitos: 
- [ ]  Conexão com banco
- [ ]  /get - listar vídeos
- [ ]  /post - inserir vídeo (id, title, duration)
- [ ]  /delete - deleta um vídeo
- [ ]  /patch - alterar vídeo (replace)
- [ ]  Documentação do swagger atualizada
- [ ]  README atualizado com: funcionalidades, bugs ou observações e pontos de melhoria ou evoluções

#### DOCUMENTAÇÕES OBRIGATÓRIAS
*   Como usar a solução
*   Passo a passo para deploy

#### SUGESTÃO DE MELHORIAS
*   Permitir inserção de vídeo de outros provedores além do youtube
*   Autenticação


## Iniciar o projeto localmente
````bash
flask run --host=0.0.0.0 --port=3333 --debug
````
#### Informações adicionais do comando:
 *  ````bash
    flask run # É o comando padrão de execução.
    ```` 
 * ````bash
    flask run --host=0.0.0.0 --port=3333 # Expõe o servidor na rede e na porta 3333.
    ````
   
 * ````bash
    flask run --debug # Faz o servidor ficar em watch mode e tem um debugger interativo no navegador.
    ````
    