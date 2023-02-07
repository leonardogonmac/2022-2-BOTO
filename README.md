# 2022/2-BOTO
<div align="center">
    <img src="https://github.com/fga-eps-mds/2022-2-BOTO/blob/main/assets/img/icon.png" height="400px" width="400px"></img>
</div>

<div align="center">

  <a href="">[![Maintainability](https://api.codeclimate.com/v1/badges/cf4ab80835f1ec26d2ff/maintainability)](https://codeclimate.com/github/fga-eps-mds/2022-2-BOTO/maintainability)</a> <a href='https://coveralls.io/github/fga-eps-mds/2022-2-BOTO?branch=main'><img src='https://coveralls.io/repos/github/fga-eps-mds/2022-2-BOTO/badge.svg?branch=main' alt='Coverage Status' /></a>
</div>




# <h1 align="center"> BOTO </h1>
Esse repostório é destinado para atualizar, modificar e informar aos usuários e/ou contribuintes do repositório sobre o nosso bot BOTO.

## :dolphin: O que é o BOTO

O BOTO é um bot do telegram que facilita aos professores enviarem conteúdos para seus alunos, desta forma ele recebe uma base de dados dos conteúdos de uma disciplina e distribui aos alunos que assinaram o bot, esses podem ser vídeos, exercícios, curiosidades e etc.

## :space_invader: Tecnologias utilizadas
- Python
- MySQL
- MySQL Workbench
- Spring Boot
- Javascript
- React JS

## :scroll: Guia de uso do BOTO

#### Instalando e executando
``````
    git clone https://github.com/fga-eps-mds/2022-2-Squad02
``````
#### Parte do Banco De Dados

Crie um banco de dados com as configurações que estão no arquivo docs/SQL_BOTO_script.sql.

Em Boto/src/conexãoDataBase/databaseBOTO.py insira as informações do seu banco de dados.

E em autenticacao-professor/src/main/resources/application.properties insira as informações do seu banco de dados.

#### Parte do Bot
* Abra o projeto e no terminal digite:

``````
    $ pip install -r requirements.txt
````````    
#### Parte do Cadastro do Professor

```
 Para conseguir utilizar o FrontEnd:

1 - Tenha instalado na sua máquina o projeto que inclui o back-end e o front-end;
2 - Baixe o node.js(https://nodejs.org/en/), selecione a opção 18.14.0 LTS;
3 - No prompt de comando do seu PC, dê esse comando "npm install -g yarn", Para instalar o YARN.
4 - No prompt de comando do seu PC, dê esse comando "npm install -g create-react-app", Para instalar o react.
5 - No prompt de comando do seu PC, dê o comando "cd C:\2022-BOTO\autenticacao-professor-app", em seguida dê esse outro comando "yarn add bootswatch" para instalar o bootswatch;
6 - No prompt de comando do seu PC, dê o comando "cd C:\2022-BOTO\autenticacao-professor-app", em seguida dê esse outro comando "yarn add react-router-dom@5.1.2"
7 - No prompt de comando do seu PC, dê o comando "cd C:\2022-BOTO\autenticacao-professor-app", em seguida dê esse outro comando "yarn add axios";
8 - No prompt de comando do seu PC, dê o comando "cd C:\2022-BOTO\autenticacao-professor-app", em seguida dê esse outro comando "yarn add toastr";
9 - Após ter feito toda essa instalação, no prompt de comando, dê o seguinte comando "cd C:\2022-BOTO\autenticacao-professor-app", em seguida dê esse outro comando "yarn start", para que a aplicação comece a rodar.
10 - Logo em seguida, abra o back-end e navegue nas páginas: "src/main/java/com/boto/autenticacaoprofessor/AutentticacaoProfessorApplication" e clique em "run" para o back começar a rodar e conseguir se cadastrar. 
`````
### Utilização
- Consiga DOIS Token em [BotFather](https://telegram.me/BotFather)
- Um dos tokens é para o bot aluno e outro para o bot professor
- Vá em Boto/src/boto_aluno.py
- Insira o TOKEN aluno no arquivo.
- Vá em Boto/src/boto_prof.py
- Insira o TOKEN professor no arquivo.
- Rode os arquivos boto_prof.py e boto_aluno.py

# Squad 2

|               Nome                 | Matrícula | GitHub                             |
|------------------------------------|---------- |------------------------------------|
| Ana Beatriz Noberto da Silva       | 211041080 | https://github.com/ananorberto     |
| Ana Luíza Fernandes Alves da Rocha | 211030667 | https://github.com/anafernanndess  |
| Beatriz Vieira Nascimento          | 211031628 | https://github.com/Beatrizvn       |                
| Geovanna Maciel Avelino da Costa   | 202016328 | https://github.com/manuziny        |
| Leonardo Gonçalves Machado         | 211029405 | https://github.com/leonardogonmac  |
| Mylena Angélica Silva Farias       | 211029497 | https://github.com/Mylena-angelica |
| Tales Rodrigues Gonçalves          | 211041295 | https://github.com/TalesRG         |


