from datetime import datetime
from loguru import logger
import pandas as pd
from util.txt import Precos
from util.tempo import Tempo
from util.constants import CSV_PATH

class ProcessadorDadosPrecos:
    def __init__(self):
        self.linhas: list[str] = self._read_precos_txt()
        self.data: pd.DataFrame = self._processar()

    def listas_para_df(self,
                       dados_titulo: list[str],
                       dados_preco: list[float],
                       dados_data: list[datetime],
                       dados_link: list[str]):
        """Essa função pega os dados de listas,
        transforma num dicionário e retorna uma DataFrame

        Args:
            dados_titulo (list[str]): lista de string com os titulos
            dados_preco (list[float]): lista de float com os valores
            dados_data (list[datetime]): lista de datetime com as datas
            dados_link (list[str]): lista de string com os links

        Returns:
            {dataframe}: retorna uma dataframe criada com as listas de indice de mesmo tamanho
        """
        tamanho_listas = self._verifica_tamanho_listas(dados_titulo,
                                                      dados_preco,
                                                      dados_data,
                                                      dados_link)
        
        if tamanho_listas == 1:

            dados = {
                "titulo": dados_titulo,
                "preco": dados_preco,
                "data": dados_data,
                "link": dados_link
            }
            data = pd.DataFrame(data=dados)
            return data

    def precos_txt_para_csv(self):
        self._processar()
        self.data.to_csv(CSV_PATH)

    def _read_precos_txt(self):
        linhas = Precos().get_linhas()
        return linhas

    def _processar(self) -> pd.DataFrame:
        entrada = self.linhas
        
        dados_titulo: list[str] = []
        dados_preco: list[str] = []
        dados_data: list[str] = []
        dados_link: list[str] = []

        titulo: str
        preco: float
        data: datetime
        link: str

        for linha in entrada:
            if linha != "":
                titulo, preco, data, link = linha.split(" | ")

                titulo = str(titulo)
                preco = float(preco)
                data = Tempo().string_to_datetime(data)
                
                dados_titulo.append(titulo)
                dados_preco.append(preco)
                dados_data.append(data)
                dados_link.append(link)

        data = self.listas_para_df(dados_titulo,
                                   dados_preco,
                                   dados_data,
                                   dados_link)
        return data

    def _verifica_tamanho_listas(self, *listas):
        """Retorna 1 se todas as listas tem o mesmo tamanho

        Raises:
            Exception: Lista vazia
            Exception: Mesmo tamanho

        Returns:
            int: 1 if todos tamanhos iguais
        """
        lista = []
        for n in listas:
            n = len(n)
            lista.append(n)
        lista = set(lista)
        if len(lista) > 1:
            logger.error(f"As listas tem tamanhos diferentes")
            raise Exception
        elif len(lista) == 0:
            logger.error(f"As listas estão vazias")
            raise Exception
        elif len(lista) == 1:
            logger.info(f"As listas tem o mesmo tamanho")
            return 1