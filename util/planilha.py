import pandas as pd
from util.txt import Precos
from util.tempo import Tempo
from util.constants import CSV_PATH, XLSX_PATH

class ProcessadorDados:
    def __init__(self):
        self.linhas: list[str]
        self.data: pd.DataFrame

        self.read_txt()
        self.processar()
        self.salvar_csv()
        self.salvar_xlsx()
        pass

    def read_txt(self):
        self.linhas = Precos().get_linhas()
        pass

    def processar(self):
        dados_titulo = []
        dados_preco = []
        dados_data = []
        for linha in self.linhas:
            titulo, preco, data = linha.split(" | ")

            titulo = str(titulo)
            preco = float(preco)
            data = Tempo().string_to_datetime(data)
            
            dados_titulo.append(titulo)
            dados_preco.append(preco)
            dados_data.append(data)
        dados = {
            "titulo": dados_titulo,
            "preco": dados_preco,
            "data": dados_data
        }
        self.data = pd.DataFrame(data=dados)
        pass

    def salvar_csv(self):
        self.data.to_csv(CSV_PATH)
        pass

    def salvar_xlsx(self):
        self.data.to_excel(XLSX_PATH)
        pass