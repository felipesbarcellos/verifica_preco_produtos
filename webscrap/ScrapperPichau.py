from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from loguru import logger


class Scrapper():
    ...

    def __init__(self, link, service):
        self.driver: webdriver.Chrome = self.configura_driver()
        self.link: str = link
        self.service: str = service

        self.titulo_produto: str
        self.preco_produto: float

        self.run()
        pass

    def run(self):
        self.acessa_link()
        self.titulo_produto = self.get_titulo_produto()
        self.preco_produto = self.get_preco_produto()

    def configura_driver(self):
        chromeoptions = Options()
        chromeoptions.add_argument("--window-position=-2500, -2500")
        driver = webdriver.Chrome(
            service=Service(
                self.service
                ),
            chrome_options=chromeoptions
            )
        return driver

    def acessa_link(self) -> None:
        self.driver.get(self.link)

    def get_titulo_produto(self) -> str:
        titulo_string = ""
        while titulo_string == "":
            try:
                titulo = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div[2]/div/div[2]/h1")
                titulo_string = titulo.text
                logger.info("O software localizou o titulo")
                logger.info(f"O título do produto é: {titulo_string}")
            except Exception as e:
                logger.warning("Não foi possível realizar a localização do elemento titulo")
                self.driver.refresh()
                contador_erros += 1
            sleep(1)
        return titulo_string

    def get_preco_produto(self) -> float:
        preco_string = ""
        while preco_string == "":
            try:
                preco = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div[2]/div")
                preco_string = preco.text
                preco_string = float(preco_string.split(" ")[1])
                logger.info("O software localizou o preço")
                logger.info(f"O preço do produto é: {preco_string}")
            except Exception as e:
                logger.warning("Não foi possível realizar a localização do elemento preço")
                self.driver.refresh()
                contador_erros += 1
            sleep(1)
        return preco_string