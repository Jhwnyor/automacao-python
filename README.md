# Automação de engajamento no instagram
Esse projeto é uma automação para engajamento de contas do instagram, usando como ferramenta **Python** e uma **biblioteca** chamada **playwright**.

## Utilidades
- link util para ler - [playwright documentação](https://playwright.dev/python/docs/intro)

## Variaveis de ambiente
Crie um arquivo na pasta raiz `app` chamado `.env` com os seguintes valores:
- SITE=https://www.instagram.com/
- EMAIL=fulano@gmail.com


## Para iniciar o projeto siga os comandos abaixo
Dentro do diretorio raiz `/automacao-python` rode:
```
poetry install
```
```
poetry shell
```
agora instale o `playwright`:
```
playwright install
```


### Gitflow
Fluxos para seguir trabalho usando o **git**


Novas funcionalidades criar branchs com prefixo `feature/funcionalidade`
Bugs criar branchs com prefixo `bugfix/importacao-errada`
