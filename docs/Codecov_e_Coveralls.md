## O que é o Codecov

- É uma ferramenra que mede a cobertura de testes do nosso código. Desta forma, mostra quais métodos e instruções no código não são testados;
- Ele está disponível para três repositórios compatíveis com o CodeBuild: GitHub, itHub Enterprise Server e Bitbucket;

### Como integrar o Codecov com o nosso projeto?

1. Ir para https://codecov.io/signup e cadastrar em um repositório de origem GitHub;
2. No Codecov adicionar o nosso repositório;
3. Quando as informações de token forem exibidas, escolher "Copy";
4. Adicionar o token copiado como uma variável de ambiente chamada `CODECOV_TOKEN` ao nosso projeto de compilação;
5. Criar um arquivo de texto chamado `my_script.sh` no repositório, depois inserir o arquivo:

``````
#/bin/bash
bash <(curl -s https://codecov.io/bash) -t $CODECOV_TOKEN
``````
6. Como nosso projeto é em Python, seguimos os comandos:

``````
build:
  - pip install coverage
  - coverage run -m unittest discover
postbuild:
  - echo 'Connect to CodeCov'
  - bash my_script.sh
``````
7. Após executar uma compilação do projeto, um link para relatórios do Codecov gerados para o porjeto aparece em `logs de compilação`, usaremos esse link para visiualizar os relatórios do Codecov
8. As informações nos logs ficam assim:

```````
[Container] 2023/01/12 16:31:04 Running command bash my_script.sh

  _____          _
 / ____|        | |
| |     ___   __| | ___  ___ _____   __
| |    / _ \ / _` |/ _ \/ __/ _ \ \ / /
| |___| (_) | (_| |  __/ (_| (_) \ V /
 \_____\___/ \__,_|\___|\___\___/ \_/
                              Bash-20200303-bc4d7e6

·[0;90m==>·[0m AWS CodeBuild detected.
... The full list of Codecov log entries has been omitted for brevity ...
    ·
    ·[0;32m->·[0m View reports at ·[0;36mhttps://codecov.io/github/user/test_py/commit/commit-id·[0m

[Container] 2020/03/09 16:31:07 Phase complete: POST_BUILD State: SUCCEEDED
```````

## O que é Coveralls

- Também é uma ferramenta de testes como o Codecov que gera relatórios sobre os testes do nosso projeto. Agora vamos ver uma forma de executar os testes localmente, com o conjunto de comandos que mostrarei abaixo:

### Instalaçaõ

``````
pip install coveralls
``````

> Após a instalação do módulo, se criará um script de linha de comando chamado `coverage`, para a versão 2.7 do Python podemos utilizar o comando `coverage` ou `coverage2`, para a versão 3 `coverage3`.

### Gerando relatórios

``````
coverage run --source=nomedopacote setup.py test
``````
> esse comando irá coletar dados do código fonte, mas caso usemos o repositório, serua por exemplo:

``````
coverage run --source=codigo_no_rep setup.py test
``````

> executando o comando `ls -la` no terminal, veremos o arquivo `.coverage`, ele contém informações sobre o nosso código.

``````
coverage report
``````

> Com esse comando, um relatório com a porcentagem de cobertura de testes de cada arquivo de código fonte será exibido no terminal. Das colunas exibidas, podemos extrair:

> Smts: indica o total de trechos do código que devem ser testados.

> Miss: coluna que indica quantos trechos do código ainda não estão sob testes.

> Cover: indica a porcentagem de cobertura de testes do arquivo fonte.

> Em `TOTAL`temos a porcentagem da cobertura total dos testes, conseguir uma porcentagem perto de 80% é satisfatório para o Coveralls.








