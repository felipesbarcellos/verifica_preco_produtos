import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from util.constants import CHROME_DRIVER_PATH
from util.txt import Precos
from util.tempo import Tempo
from util.planilha import ProcessadorDadosPrecos
from loguru import logger

class Scrapper:
    def __init__(self):
        self.driver: webdriver.Chrome = self.configura_driver()
        self.arquivo_precos_txt = Precos()
        self.titulo_produto: str
        self.preco_produto: float
        self.url: str
        self.hoje: str = Tempo().get_data_hoje_str()
        self.processador_dados = ProcessadorDadosPrecos()
        pass

    def run(self):
        try:
            self.acessa_link(self.url)
            self.titulo_produto = self.get_titulo_produto()
            self.preco_produto = self.get_preco_produto()
            self.driver.close()
            self.salvar_saida_precos_csv()
        except Exception as e:
            raise e

    def configura_driver(self):
        chromeoptions = Options()
        chromeoptions.add_argument("--window-position=-2500, -2500")
        chromeoptions.page_load_strategy = "eager"
        driver = webdriver.Chrome(
            service=Service(
                CHROME_DRIVER_PATH
                ),
            chrome_options=chromeoptions
            )
        driver.implicitly_wait(3)
        return driver
    
    def acessa_link(self, url) -> None:
        self.driver.get(url)

    def salvar_saida_precos_txt(self):
        self.arquivo_precos_txt.salvar_preco(self.titulo_produto, self.preco_produto, self.hoje, self.url)

    def salvar_saida_precos_csv(self):
        data: pd.Dataframe = self.processador_dados.lista_para_df(self.titulo_produto, self.preco_produto, self.hoje, self.url)
        self.processador_dados.salvar_df_csv_precos(data)

        ...