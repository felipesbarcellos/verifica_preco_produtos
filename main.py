from util.constants import *
from util.txt import Links, Precos
from webscrap.ScrapperPichau import ScrapperPichau
from util.planilha import ProcessadorDados

scrappers = []

def get_scrapper_por_url(url: str):
    if url.startswith("https://www.pichau.com.br/"):
        scrappers.append(ScrapperPichau(url))

arquivo_link = Links()
arquivo_precos = Precos()

links = arquivo_link.get_linhas()

arquivo_link.cria_arquivo()
arquivo_precos.cria_arquivo()

for link in links:
    # logger.debug(f"Link selecionado: {link}")

    get_scrapper_por_url(link)
    ...

ProcessadorDados()