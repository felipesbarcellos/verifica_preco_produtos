# Verificador de preços de produtos da Pichau
## Sobre o repositório
Criei o repositório com o intuito de monitorar o preço de alguns produtos da Pichau de forma mais eficiente e automatizada.

## Tecnologias
No desenvolvimento desse projeto foram usadas as seguintes tecnologias

bibliotecas:
- loguru
- webdriver_manager

framework:
- selenium (e todas suas dependencias)

linguagem de programação:
- python

## Instalação e utilização
Requisitos: [Python](https://www.python.org/downloads/)

1. Abra o terminal e entre na pasta do projeto ex: ```cd Desktop/pasta_do_software```
2. Na pasta do projeto, execute o comando: ```python -m venv venv```
3. Depois execute``` venv\Scripts\python -m pip install -r requirements.txt```
4. Para rodar execute ```venv\Scripts\python main.oy```
5. *Coloque os links da pichau no arquivo *links.txt** (pode criar um atalho para ele se precisar)
7. Espere o software processar os dados
8. *Verifique o arquivo *precos.txt* para encontrar o resultado*

## Observações
Os arquivos link.txt e precos.txt podem ser alterados. Alguns dados já vem por padrão para demonstrar a funcionalidade, mas podem ser apagados.
