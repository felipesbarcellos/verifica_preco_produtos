from selenium.webdriver.common.by import By
from time import sleep
from loguru import logger
from webscrap.Scrapper import Scrapper


class ScrapperTerabyte(Scrapper):

    def __init__(self, url):
        super().__init__()
        self.url: str = url
        self.run()


    def get_titulo_produto(self) -> str:
        titulo_string = ""
        while titulo_string == "":
            try:
                try:
                    titulo = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[3]/div/div/h1")
                except:
                    pass
                try:
                    titulo = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[3]/div/h1")
                except:
                    pass
                # /html/body/div[4]/div[2]/div/div/div[3]/div/h1
                titulo_string = titulo.text
                logger.info("O software localizou o titulo")
                logger.info(f"O título do produto é: {titulo_string}")
            except Exception as e:
                logger.warning("Não foi possível realizar a localização do elemento titulo")
                logger.error(e)
                self.fecha_pop_up()
                # self.driver.refresh()
            sleep(1)
        return titulo_string

    def get_preco_produto(self) -> float:
        preco = ""
        while preco == "":
            try:
                try:
                    preco_element = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[3]/div/div/div[10]/div[2]/div[1]/div/p[2]")
                except:
                    pass
                try:
                    preco_element = self.driver.find_element(By.ID, "valVista")
                except:
                    pass
                preco_string = preco_element.text
                preco_string = preco_string.split(' ')[1]
                reais = int(preco_string.split(',')[0].replace('.',''))
                centavos = int(preco_string.split(',')[1])
                preco = float(f"{reais}.{int(str(centavos)[:2])}")
                
                logger.info("O software localizou o preço")
                logger.info(f"O preço do produto é: R$ {preco}")
            except Exception as e:
                logger.warning("Não foi possível realizar a localização do elemento preço")
                self.fecha_pop_up()
                # self.driver.refresh()
            sleep(1)
        return preco
    
    def fecha_pop_up(self):
        try:
            close_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/button/span")
            close_button.click()
            logger.trace("A função fecha_pop_up foi realizada.")
        except:
            logger.trace("A função fecha_pop_up foi ignorada.")
