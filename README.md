# Verificador de preços de produtos da Pichau
## Sobre o repositório
Software desktop com python e pandas para monitorar o preço de uma lista de produtos. Disponível: Pichau, Terabyte, Amazon, MagazineLuiza e Mercado Livre.

## Lojas disponíveis:
- Amazon
- Mercado Livre
- Magazine Luiza
- Terabyte
- Pichau

## Tecnologias
As seguintes tecnologias foram utilizadas no desenvolvimento deste projeto

bibliotecas:
- loguru
- webdriver_manager

framework:
- selenium (e todas suas dependências)

linguagem de programação:
- python

## Requisitos
- [Python](https://www.python.org/downloads/) 3.8 ou superior
- Google Chrome instalado
- Conexão com a internet

## Instalação
1. Abra o terminal e entre na pasta do projeto ex: ```cd Downloads/pasta_do_software```
2. Na pasta do projeto, execute o comando: ```python -m venv venv```
3. Depois execute ```venv\Scripts\python -m pip install -r requirements.txt```

## Utilização
1. Coloque os links da Pichau no arquivo links.txt (pode criar um atalho para ele se precisar)
2. Para rodar execute ```venv\Scripts\python main.py``` ou execute o run.bat
3. Espere o software realizar a raspagem dos dados
4. Verifique o arquivo precos.csv com auxilio de um software de planilhas para visualizar o resultado

## Estrutura do Projeto
- `main.py` - Arquivo principal que inicia o programa
- `webscrap/` - Contém os scripts de raspagem para cada loja
- `data/` - Pasta com arquivos de entrada e saída
  - `links.txt` - Lista de URLs dos produtos para monitorar
  - `precos.csv` - Arquivo de saída com os preços coletados
- `util/` - Módulos utilitários do projeto
- `drivers/` - Pasta com drivers do navegador

## Formato dos Arquivos
### links.txt
- Um link por linha
- Aceita links de qualquer uma das lojas suportadas

### precos.csv
Colunas do arquivo de saída:
- Nome do produto
- Preço
- Data da coleta
- URL do produto

## Solução de Problemas
- Se o Chrome não iniciar, verifique se está instalado corretamente
- Certifique-se que o arquivo links.txt existe e contém URLs válidas
- Em caso de erro de conexão, verifique sua internet
- Se o driver do Chrome apresentar problemas, ele será baixado automaticamente na primeira execução

## Observações
O arquivo links.txt pode ser alterado. Alguns dados já virão por padrão para demonstrar a funcionalidade, mas podem ser apagados.
