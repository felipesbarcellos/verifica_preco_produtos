from webscrap.Scrapper import Scrapper
from selenium.webdriver.common.by import By


class ScrapperMercado(Scrapper):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def get_titulo_produto(self):
        titulo_string: str = ""
        while titulo_string == "":
            try:
                titulo_element = self.driver.find_element(By.CLASS_NAME,"ui-pdp-title")
                titulo_string = titulo_element.text
                return titulo_string
            except Exception as e:
                raise e
    
    def get_preco_produto(self):
        preco_element = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span/span[2]")
        preco_string: str = preco_element.text
        preco: float = float(preco_string)
        return preco
