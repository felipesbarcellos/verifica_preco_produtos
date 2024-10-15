from time import sleep
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
