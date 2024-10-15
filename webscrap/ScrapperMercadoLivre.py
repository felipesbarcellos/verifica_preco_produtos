from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from loguru import logger
from util.constants import CHROME_DRIVER_PATH, PRECOS_PATH
from webscrap.Scrapper import Scrapper

class ScrapperMercadoLivre(Scrapper):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        ...

    def get_titulo_produto(self) -> str:
        ...

    def get_preco_produto(self) -> float:
        ...
