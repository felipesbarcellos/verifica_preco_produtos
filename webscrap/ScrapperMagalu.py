from webscrap.Scrapper import Scrapper
from selenium.webdriver.common.by import By


class ScrapperMagalu(Scrapper):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def get_titulo_produto(self):
        titulo_string: str = ""
        while titulo_string == "":
            try:
                titulo_element = self.driver.find_element(By.XPATH,"//h1[@data-testid='heading-product-title']")
                titulo_string = titulo_element.text
                return titulo_string
            except Exception as e:
                    raise e
    
    def get_preco_produto(self):
        preco_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[7]/div[6]/div/div/div/div/p")
        preco_string: str = preco_element.text
        preco = preco_string.split(' ')[-1]
        inteiro = preco.split(',')[0].replace(".","")
        decimos = preco.split(',')[1]
        preco: float = float(f"{inteiro}.{decimos}")
        return preco
