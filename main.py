from util.constants import *
import pandas as pd
from util.txt import Links, Precos
from webscrap.ScrapperPichau import ScrapperPichau
from webscrap.ScrapperTerabyte import ScrapperTerabyte
from loguru import logger
from util.planilha import ProcessadorDadosPrecos

class Main:
    def __init__(self):
        self.scrappers: list = []
        self.dados: pd.DataFrame = ProcessadorDadosPrecos().data
        self.arquivo_link = Links()
        self.arquivo_precos = Precos()

        self.links = self.arquivo_link.get_linhas()

        self._verificar_integridade_arquivos_txt()

    def executar_iteracao(self):
        for link in self.links:
            self._executar(link)

    def _executar(self, link):
        try:
            logger.debug(f"Link selecionado: {link}")
            self._get_scrapper_por_url(link)
            ProcessadorDadosPrecos().precos_txt_para_csv()

        except Exception as e:
            logger.error(f"Ocorreu um erro:\n{e}\n")

    def _verificar_integridade_arquivos_txt(self):
        self.arquivo_link.cria_arquivo()
        self.arquivo_precos.cria_arquivo()

    def _get_scrapper_por_url(self, url: str):
        site = url.split(".")[1]
        logger.trace(f"Selecionado: {site}")
        if url.startswith("https://www.pichau.com.br/"):
            try:
                self.scrappers.append(ScrapperPichau(url).run())
            except Exception as e:
                logger.error(f"Houve um erro ao acessar a {site}\n{e}\n")

        elif url.startswith("https://www.terabyteshop.com.br/"):
            try:
                self.scrappers.append(ScrapperTerabyte(url).run())
            except Exception as e:
                logger.error(f"Houve um erro ao acessar a {site}\n{e}\n")


if __name__ == "__main__":
    Main().executar_iteracao()
    ...