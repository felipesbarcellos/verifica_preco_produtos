from webscrap.Scrapper import Scrapper
from selenium.webdriver.common.by import By


class ScrapperAmazon(Scrapper):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def get_titulo_produto(self):
        titulo_string: str = ""
        while titulo_string == "":
            try:
                titulo_element = self.driver.find_element(By.ID,"productTitle")
                titulo_string = titulo_element.text
                return titulo_string
            except Exception as e:
                if "?th=1" in self.driver.current_url:
                    url_sem_autenticacao = self.driver.current_url[:-5]
                    self.driver.get(url_sem_autenticacao)
                else:
                    raise e
    
    def get_preco_produto(self):
        preco_element = self.driver.find_element(By.CLASS_NAME, "a-price-whole")
        preco_string: str = preco_element.text
        preco: float = float(preco_string)
        return preco
