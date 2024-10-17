from selenium.webdriver.common.by import By
from time import sleep
from loguru import logger
from webscrap.Scrapper import Scrapper


class ScrapperPichau(Scrapper):

    def __init__(self, url):
        super().__init__()
        self.url: str = url
        #self.run()


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
                # self.driver.refresh()
            sleep(1)
        return titulo_string

    def get_preco_produto(self) -> float:
        preco = ""
        while preco == "":
            try:
                preco_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div[2]/div")
                preco_string = preco_element.text
                preco_string = preco_string.split(' ')[1]
                reais = int(preco_string.split(',')[0])
                centavos = int(preco_string.split(',')[1])
                preco = float(f"{reais}.{int(str(centavos)[:2])}")
                
                logger.info("O software localizou o preço")
                logger.info(f"O preço do produto é: R$ {preco}")
            except Exception as e:
                logger.warning("Não foi possível realizar a localização do elemento preço")
                logger.error(e)
                # self.driver.refresh()
            sleep(1)
        return preco