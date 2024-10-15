from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from util.constants import CHROME_DRIVER_PATH, PRECOS_PATH
from util.txt import Precos
from loguru import logger
from util.hoje import Hoje

class Scrapper:
    def __init__(self):
        self.driver: webdriver.Chrome = self.configura_driver()
        self.arquivo_saida = Precos(PRECOS_PATH)
        self.titulo_produto: str
        self.preco_produto: float
        pass

    def run(self):
        try:
            self.acessa_link()
            self.titulo_produto = self.get_titulo_produto()
            self.preco_produto = self.get_preco_produto()
            self.driver.close()
            self.salvar_saida()
        except Exception as e:
            logger.error(e)
            pass

    def configura_driver(self):
        chromeoptions = Options()
        chromeoptions.add_argument("--window-position=-2500, -2500")
        driver = webdriver.Chrome(
            service=Service(
                CHROME_DRIVER_PATH
                ),
            chrome_options=chromeoptions
            )
        driver.implicitly_wait(10)
        return driver
    
    def acessa_link(self) -> None:
        self.driver.get(self.url)

    def salvar_saida(self):
        self.arquivo_saida.salvar_preco(self.titulo_produto, self.preco_produto, Hoje())
