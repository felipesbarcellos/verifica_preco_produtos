from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from loguru import logger
from datetime import datetime
from util.constants import *
from util.hoje import Hoje

with open(LINKS_PATH, mode='r', encoding="utf-8") as f:
    links = f.readlines()


def cria_arquivo(nome):
    try:
        f = open(nome, mode="x")
        f.close()
        # logger.debug(f"Arquivo {nome} criado com sucesso!")
    except FileExistsError:
        # logger.debug(f"O arquivo {nome} já existe")
        pass

cria_arquivo(LINKS_PATH)
cria_arquivo(PRECOS_PATH)

NOME_ARQUIVO = LINKS_PATH

# try:
    # service = ChromeDriverManager().install()
    # logger.debug("O driver foi baixado com sucesso.")
# except Exception as e:
    # logger.error(f"\nOcorreu um erro ao tentar baixar o driver:\n{e}\n")

def get_data_hoje() -> str:
    hoje = datetime.today()
    dia = hoje.day
    mes = hoje.month
    ano = hoje.year

    data = f"{dia}/{mes}/{ano}"
    return data

for link in links:
    # logger.debug(f"Link selecionado: {link}")

    try:
        chromeoptions = Options()
        # chromeoptions.add_argument("--window-position=-2500, -2500")
        driver = webdriver.Chrome(
            
                DRIVER_PATH
            )
        # driver.maximize_window()
        driver.get("www.google.com")
        driver.implicitly_wait(10)
        # logger.debug(driver.capabilities['chrome']['chromedriverVersion'])

        # driver.set_window_position(-2000, -2000)
        # logger.debug(f"O driver foi construido com sucesso!")
    except Exception as e:
        logger.error(f"\nOcorreu um erro ao tentar construir o driver:\n{e}\n")

    try:
        driver.get(link)
    except Exception as e:
        logger.error(f"\nOcorreu um erro ao tentar acessar o link:\n{e}\n")

    contador_erros = 0
    if contador_erros >= 5:
        logger.warning(f"Ocorreram erros demais, a página está sendo reinicializada.")
        driver.get(link)

    preco_string = ""
    while preco_string == "":
        try:
            preco = driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div[2]/div")
            preco_string = preco.text
            logger.info("O software localizou o preço")
            logger.info(f"O preço do produto é: {preco_string}")
        except Exception as e:
            logger.warning("Não foi possível realizar a localização do elemento preço")
            driver.refresh()
            contador_erros += 1
        sleep(1)

    titulo_string = ""
    while titulo_string == "":
        try:
            titulo = driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div[2]/div/div[2]/h1")
            titulo_string = titulo.text
            logger.info("O software localizou o titulo")
            logger.info(f"O título do produto é: {titulo_string}")
        except Exception as e:
            logger.warning("Não foi possível realizar a localização do elemento titulo")
            contador_erros += 1
        sleep(1)
    driver.close()
    data = get_data_hoje()
    # logger.debug(f"hoje é: {data}")
    with open(NOME_ARQUIVO, mode="a", encoding="utf-8") as f:
        f.write(f"{titulo_string} | {preco_string} | {Hoje()}\n")