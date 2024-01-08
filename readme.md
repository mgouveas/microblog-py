# Backend de uma aplicação de microblog _(Twitter)_

### Projeto desenvolvido para replicar funcionalidades básicas (Criar, Listar e Curtir postagens) de um sistema de microblog (twitter) implementado à partir de uma versão inicialmente desenvolvida em _Javascript e NodeJS_.

## Funcionalidades:

* Criar publicação
* Listar publicações
* Curtir uma publicação

## Regras da API

### A API integra o sistema com o banco de dados em MongoDB

* ### Criar postagem (methods='POST', rota='/tweets'):
  * No corpo da requisição é necessário conter apenas as chaves "author" e "content"
  * As chaves "_id", "likes" e "createdAt" são criadas automaticamente
  * A chave "likes" inicia com o valor padrão 0

* ### Listar postagens (methods='GET', rota='/tweets'):
  * Retorna todas as publicações criadas

* ### Curtir publicação (methods='POST', rota='/likes'):
  * No corpo da requisição é passado apenas o id da publicação no banco
  * A variável tweet_like recebe o id da requisição e dispara uma ação de update no banco fazendo o incremento do valor da chave 'likes'

## Próximos passos
  
  * Futuramente o sistema irá receber atualização em sua estrutura, retirando todas as funcionalidades e rotas do arquivo principal 'index.py';

## 🛠 Techs Stack

<div style="display: inline_block"><br>
  <img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>