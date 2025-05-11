import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from util.constants import CHROME_DRIVER_PATH
from util.log import Log
from util.txt import Precos
from util.tempo import Tempo
from util.planilha import DadosPreco
from loguru import logger
from webdriver_manager.chrome import ChromeDriverManager

class Scrapper:
    def __init__(self):
        self.driver: webdriver.Chrome = self._configura_driver()
        self.arquivo_precos_txt = Precos()
        self.titulo_produto: str
        self.preco_produto: float
        self.url: str
        self.hoje: str = Tempo().get_data_hoje_str()
        self.processador_dados = DadosPreco()
        pass

    def run(self):
        try:
            self.acessa_link(self.url)
            self.raspar()
            log = Log()
            log.preco_produto_localizado(self.preco_produto)
            log.nome_produto_localizado(self.titulo_produto)
            self.driver.close()
            self.salvar_saida_precos_csv()
        except Exception as e:
            raise e

    def raspar(self):
        tentativas = 3
        while tentativas != 0:
            self.titulo_produto = self._get_titulo_produto()
            self.preco_produto = self._get_preco_produto()
            if self.titulo_produto != "" and self.preco_produto != "":
                break
            else:
                tentativas -= 1
                logger.warning("Tentando novamente")
                if tentativas == 0:
                    logger.error("Tentativas esgotadas")
                    raise Exception("Tentativas esgotadas")
    
    def acessa_link(self, url) -> None:
        self.driver.get(url)

    def salvar_saida_precos_csv(self):
        data: pd.Dataframe = self.processador_dados.lista_para_df(self.titulo_produto, self.preco_produto, self.hoje, self.url)
        self.processador_dados.salvar_df_csv_precos(data)

    def _get_titulo_produto(self) -> str:
        pass

    def _get_preco_produto(self) -> float:
        pass

    def _configura_driver(self):
        chromeoptions = Options()
        chromeoptions.add_argument("--window-position=-2500, -2500")
        chromeoptions.page_load_strategy = "eager"
        chromeoptions.add_argument("--no-sandbox")
        chromeoptions.add_argument("--disable-dev-shm-usage")
        # chromeoptions.add_argument("--headless")
        
        # Tratamento do handshake SSL
        chromeoptions.add_argument("--ignore-certificate-errors")
        chromeoptions.add_argument("--incognito")
        
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chromeoptions
        )
        
        driver.implicitly_wait(5)
        return driver

    # def salvar_saida_precos_txt(self):
    #     self.arquivo_precos_txt.salvar_preco(self.titulo_produto, self.preco_produto, self.hoje, self.url)