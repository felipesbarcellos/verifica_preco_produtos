from util.constants import *
import pandas as pd
from util.txt import Links, Precos
from webscrap.ScrapperPichau import ScrapperPichau
from webscrap.ScrapperTerabyte import ScrapperTerabyte
from util.planilha import ProcessadorDados

scrappers = []

def get_scrapper_por_url(url: str):
    if url.startswith("https://www.pichau.com.br/"):
        scrappers.append(ScrapperPichau(url))
    elif url.startswith("https://www.terabyteshop.com.br/"):
        scrappers.append(ScrapperTerabyte(url))

dados: pd.DataFrame = ProcessadorDados().data
arquivo_link = Links()
arquivo_precos = Precos()

links = arquivo_link.get_linhas()

arquivo_link.cria_arquivo()
arquivo_precos.cria_arquivo()

for link in links:
    try:
        dados = dados.loc([dados["link"] == link])
    except Exception as e:
        print(f"erro: \n{e}")
        pass
    # logger.debug(f"Link selecionado: {link}")

    get_scrapper_por_url(link)
    ...

ProcessadorDados()