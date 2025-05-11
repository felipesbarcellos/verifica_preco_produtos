from selenium.webdriver.common.by import By
from loguru import logger
from webscrap.Scrapper import Scrapper


class ScrapperPichau(Scrapper):

    def __init__(self, url):
        super().__init__()
        self.url: str = url
        #self.run()


    def _get_titulo_produto(self) -> str:
        titulo_string = ""
        while titulo_string == "":
            try:
                titulo = self.driver.find_element(By.CSS_SELECTOR, "[data-cy='product-page-title']")
                titulo_string = titulo.text
                logger.info("O software localizou o titulo")
                logger.info(f"O título do produto é: {titulo_string}")
            except Exception as e:
                logger.warning("Não foi possível realizar a localização do elemento titulo")
                # self.driver.refresh()
        return titulo_string

    def _get_preco_produto(self) -> float:
        preco = ""
        while preco == "":
            try:
                preco_element = self.driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div[2]/div[2]")
                preco_string = preco_element.text
                preco_string = preco_string.split(' ')[1]
                reais = int(preco_string.split(',')[0])
                centavos = int(preco_string.split(',')[1])
                preco = float(f"{reais}.{int(str(centavos)[:2])}")
                
            except Exception as e:
                try:
                    self.driver.find_element(By.XPATH, "//*[text()='OK']").click()
                    continue
                except:
                    pass
                logger.warning("Não foi possível realizar a localização do elemento preço")
                logger.warning("Tentando novamente")
                logger.error(e)
                # self.driver.refresh()
        return preco