from datetime import datetime
import pandas as pd
from util.txt import Precos
from util.tempo import Tempo
from util.constants import CSV_PATH

class ProcessadorDados:
    def __init__(self):
        self.linhas: list[str]
        self.data: pd.DataFrame = self._processar()

    def para_csv(self):
        self._processar()
        self.data.to_csv(CSV_PATH)

    def _read_txt(self):
        self.linhas = Precos().get_linhas()

    def _processar(self) -> pd.DataFrame:
        self._read_txt()
        dados_titulo: list[str] = []
        dados_preco: list[str] = []
        dados_data: list[str] = []
        dados_link: list[str] = []

        titulo: str
        preco: float
        data: datetime
        link: str

        for linha in self.linhas:
            if linha != "":
                titulo, preco, data, link = linha.split(" | ")

                titulo = str(titulo)
                preco = float(preco)
                data = Tempo().string_to_datetime(data)
                
                dados_titulo.append(titulo)
                dados_preco.append(preco)
                dados_data.append(data)
                dados_link.append(link)

        dados = {
            "titulo": dados_titulo,
            "preco": dados_preco,
            "data": dados_data,
            "link": dados_link
        }
        data = pd.DataFrame(data=dados)
        return data