from util.constants import *
import pandas as pd
from util.txt import Links
from webscrap.ScrapperPichau import ScrapperPichau
from webscrap.ScrapperTerabyte import ScrapperTerabyte
from webscrap.ScrapperAmazon import ScrapperAmazon
from webscrap.ScrapperMagalu import ScrapperMagalu
from webscrap.ScrapperMercado import ScrapperMercado
from loguru import logger
from util.planilha import DadosPreco

class Main:
    def __init__(self):
        
        self.scrappers: list = []
        self.arquivo_link = Links()
        self.processador_dados = DadosPreco()

        self.links = self.arquivo_link.get_linhas()

        self._verificar_integridade_arquivos_txt()

    def executar_iteracao(self):
        for link in self.links:
            self._executar(link)

    def _executar(self, link):
        # try:
        logger.debug(f"Link selecionado: {link}")
        self._get_scrapper_por_url(link)

        # except Exception as e:
        #     logger.error(f"Ocorreu um erro:\n{e}\n")

    def _verificar_integridade_arquivos_txt(self):
        self.arquivo_link.cria_arquivo()

    def _get_scrapper_por_url(self, url: str):
        site_nome = url.split(".")[1]
        logger.trace(f"Selecionado: {site_nome}")

        pichau_url = "https://www.pichau.com.br/"
        terabyte_url = "https://www.terabyteshop.com.br/"
        amazon_url = "https://www.amazon.com.br/"
        magazine_url = "https://www.magazineluiza.com.br/"
        mercado_url = "https://www.mercadolivre.com.br/"

        if url.startswith(pichau_url):
            self.scrappers.append(ScrapperPichau(url).run())
            # logger.error(f"Houve um erro ao acessar a {site_nome}\n{e}\n")

        elif url.startswith(terabyte_url):
            self.scrappers.append(ScrapperTerabyte(url).run())

        elif url.startswith(amazon_url):
            self.scrappers.append(ScrapperAmazon(url).run())

        elif url.startswith(magazine_url):
            self.scrappers.append(ScrapperMagalu(url).run())

        elif url.startswith(mercado_url):
            self.scrappers.append(ScrapperMercado(url).run())


if __name__ == "__main__":
    Main().executar_iteracao()
    ...