import pandas as pd
from selenium.webdriver.common.by import By
from loguru import logger
from webscrap.Scrapper import Scrapper


class ScrapperTerabyte(Scrapper):

    def __init__(self, url):
        super().__init__()
        self.url: str = url
        # self.run()


    def _get_titulo_produto(self) -> str:
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
        return titulo_string

    def _get_preco_produto(self) -> float:
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
                
            except Exception as e:
                logger.warning("Não foi possível realizar a localização do elemento preço")
                self.fecha_pop_up()
                # self.driver.refresh()
        return preco
    
    def fecha_pop_up(self):
        try:
            close_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/button/span")
            close_button.click()
            logger.trace("A função fecha_pop_up foi realizada.")
        except:
            logger.trace("A função fecha_pop_up foi ignorada.")

    def raspar_pagina(self, link_inicial):
        """Realiza o scrap de uma determinada
        categoria especificada via link inicial.
        Exemplo: {link das páginas de
        memórias ram na terabyte}"""
        self.acessa_link(link_inicial)
        
        self.produtos = self.driver.find_elements(By.CLASS_NAME, "product-item__box")
        self.titulos = []
        self.valores = []
        for produto in self.produtos:
            try:
                titulo = produto.find_element(By.CSS_SELECTOR, "a.product-item__name")
                titulo = titulo.get_attribute("title")
                logger.debug(f"titulo: {titulo}")

                valor = produto.find_element(By.CLASS_NAME, "product-item__new-price")
                valor = valor.find_element(By.TAG_NAME, "span")
                valor = valor.get_attribute("innerHTML")
                logger.debug(f"titulo: {valor}")
#
                try:
                    self.titulos.append(titulo)
                    self.valores.append(valor)
                    logger.debug("valores adicionados a lista")
                except Exception as e:
                    logger.error(f"houve um arro ao adicionar na lista: \n{e}\n")
            except Exception as e:
                logger.error(f"{e}")

        data = {
            "titulo":self.titulos,
            "valor":self.valores
        }

        df = pd.DataFrame(data=data)
        df.to_csv('data/test_data_terabyte.csv')
        logger.debug(df.head())