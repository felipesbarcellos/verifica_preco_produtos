# Verificador de preços de produtos da Pichau
## Sobre o repositório
Este software tem como objetivo monitorar os preços da Pichau com base em uma lista de links enviada pelo usuário.

## Tecnologias
No desenvolvimento desse projeto foram usadas as seguintes tecnologias

bibliotecas:
- loguru
- webdriver_manager

framework:
- selenium (e todas suas dependencias)

linguagem de programação:
- python

## Requisitos
Requisitos: [Python](https://www.python.org/downloads/)

## Instalação
1. Abra o terminal e entre na pasta do projeto ex: ```cd Desktop/pasta_do_software```
2. Na pasta do projeto, execute o comando: ```python -m venv venv```
3. Depois execute ```venv\Scripts\python -m pip install -r requirements.txt```

## Utilização
1. Coloque os links da Pichau no arquivo links.txt (pode criar um atalho para ele se precisar)
2. Para rodar execute ```venv\Scripts\python main.py```
3. Espere o software processar os dados
4. Verifique o arquivo precos.txt para encontrar o resultado

## Observações
Os arquivos link.txt e precos.txt podem ser alterados. Alguns dados já vem por padrão para demonstrar a funcionalidade, mas podem ser apagados.
