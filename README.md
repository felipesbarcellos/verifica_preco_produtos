# Verificador de preços de produtos da Pichau
## Sobre o repositório
Programa desktop que monitora o preço de uma lista de produtos. Disponível Pichau, Terabyte, Amazon, MagazineLuiza e Mercado Livre.

## Lojas disponívels:
- Amazon
- Mercado Livre
- Magazine Luiza
- Terabyte
- Pichau

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
1. Abra o terminal e entre na pasta do projeto ex: ```cd Downloads/pasta_do_software```
2. Na pasta do projeto, execute o comando: ```python -m venv venv```
3. Depois execute ```venv\Scripts\python -m pip install -r requirements.txt```

## Utilização
1. Coloque os links da Pichau no arquivo links.txt (pode criar um atalho para ele se precisar)
2. Para rodar execute ```venv\Scripts\python main.py``` ou execute o run.bat
3. Espere o software realizar a raspagem dos dados
4. Verifique o arquivo precos.csv com auxilio de um software de planilgas para visualizar o resultado

## Observações
O arquivo link.txt pode ser alterado. Alguns dados já virão por padrão para demonstrar a funcionalidade, mas podem ser apagados.
