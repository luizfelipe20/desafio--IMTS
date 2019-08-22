# Desafio IMTS

Desafio de admissão 2019.2 IMTS.


## Início

Essas instruções farão com que você tenha uma visão de como será a avaliação. Repare bem as obrigatoriedades que o processo exigirá e os bônus que estarão disponíveis para aumentar a sua pontuação
nesse teste.

A avaliação se dará através da análise da **construção** de um Servidor Flask (utilizando qualquer versão, a partir da 3, da linguagem de programação Python). 

Boas práticas de programação, desenvolvimento de padrões de projetos e controle de versão serão habilidades obrigatórias para esse desafio. Essas skills serão responsáveis por **0.6** da avaliação.

Implementações de outras habilidades: migrações e versionamento de banco de dados, emprego de ORM (Object Relational Mapper), controle de acesso às rotas do Servidor, utilização de um banco de dados em memória - Redis (implementação de alguma forma de cache, *doesn't matter*) e integração com outras API (alguma de e-mail, p.e.) serão skills responsáveis pelo resto da composição da nota: **0.4**.

Sem estresse e sem medo, abaixo está a descrição para o seu sucesso. *May be force be with you*:

![Yoda](https://www.fanthatracks.com/wp-content/uploads/2018/09/ironstudios_yoda_cover.jpg)

* O Servidor, basicamente, deverá ser responsável pelo controle de Eventos e seus respectivos Usuários. 

* Usuários devem poder se inscrever à Eventos, desde que estes estejam dentro do intervalo de inscrição do Evento. Eventos devem possuir dois intervalos: o de inscrição e o ao qual ele estará ocorrendo. Listar, editar, salvar e deletar serão funcionalidades obrigatórias para os dois modelos. Autenticar e redefinir senha exclusivos ao segundo, Usuários. A autenticação deve retornar um **token JWT**.

* Todos os modelos devem ter a capacidade de serem persistidos em um Banco de Dados relacional, [Postgresql](https://www.postgresql.org/), possuindo, assim, um identificador único universal, uma chave primária. Essa deve possuir 36 caracteres (dica, [uuid](https://pt.wikipedia.org/wiki/Identificador_%C3%BAnico_universal)). 

* O modelo de Usuários deve possuir, além do identificador universal, os seguintes atributos: nome, username, password, telefone, aniversário e e-mail.

* Já o modelo de Eventos deve ter, também além do indentificador universal: título, descrição, data início, data fim, data início inscrições, data fim inscrições.

* A funcionalidade de inscrição de Usuários à Eventos pode ser realizada tanto com uma tabela adicional, p.e. UsuarioEvento, relacionando os dois modelos, quanto com um atributo array no modelo adequado. Esta funcionalidade fica sob responsabilidade do desafiado (rsrsrs).

<p align="center">
  <img src="https://cdn.panrotas.com.br/portal-panrotas-statics/media-files-original/2016/02/23/392fef1df228f691e76cbf9ed6fd437a-02route66230216.jpg" alt="Rotas"/>
</p>

* O Servidor deve ter rotas, para validação e teste pela nossa equipe, ok? Sugestão: 
  * */login* POST recebendo `{"username": "desafiado", "password": "vdc"}`;
  * */recovery-password* POST recebendo `{"username": "desafiado"}`;
  * */users* GET, POST, PUT, DELETE;
  * */events* GET, POST, PUT, DELETE;
  * */user-event* GET, POST, PUT, DELETE;


* Lembre de separar o projeto em *branchs*. Quão mais próximo da realidade, maior será a nota.


### Instalação

Uma estrutura básica do projeto, com algumas dependências, estará disponível. Sinta-se com liberdade para editar essa arquitetura ou usá-la.

Caso opte por usá-la, algumas dependências, à nível de auxílio, estarão presentes no `requirements.txt`. Para fazer a instalação dessas dependências, aconselho a utilização de alguma biblioteca para **virtualização de ambientes** (p.e. conda ou virtualenv). Para instalar as dependências, execute, p.e.:

```
pip3 install -r requirements.txt
```

Feito a instalação das dependências mínimas, dê um *up* no Servidor:
```
python3 server.py
```


## Autores

* **Eduardo Pereira** - *Elaborador do Exame*
