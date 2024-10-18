from datetime import datetime
from loguru import logger
import pandas as pd
from util.txt import Precos
from util.tempo import Tempo
from util.constants import CSV_PATH

class DadosPreco:
    def __init__(self):
        
        self.df = self._read_csv()
        ...

    def lista_para_df(
            self,
            dados_titulo: str,
            dados_preco: float,
            dados_data: str,
            dados_link: str
            ) -> pd.DataFrame:
        """Essa função pega os dados de listas,
        transforma num dicionário e retorna uma DataFrame

        Args:
            dados_titulo (list[str]):  string com os titulos
            dados_preco (list[float]):  float com os valores
            dados_data (list[datetime]):  datetime com as datas
            dados_link (list[str]):  string com os links

        Returns:
            {dataframe}: retorna uma dataframe criada com as listas de indice de mesmo tamanho
        """

        dados = {
            "titulo": dados_titulo,
            "preco": dados_preco,
            "data": dados_data,
            "link": dados_link
        }
        data = pd.DataFrame(data=dados, index=[0])
        return data

    def salvar_df_csv_precos(self, df_nova: pd.DataFrame | None = None):
        try:
            self.df = pd.concat([self.df, df_nova], ignore_index=1)
            self.df.to_csv(CSV_PATH, index=0)
        except AttributeError:
            self.df = pd.DataFrame(df_nova)
            self.df.to_csv(CSV_PATH, index=0)
        except Exception as e:
            raise e

    def _read_csv(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(CSV_PATH)
            return df
        except Exception as e:
            df = pd.DataFrame()
            return df
            
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

        data = self.lista_para_df(dados_titulo,
                                   dados_preco,
                                   dados_data,
                                   dados_link)
        return data

    def _verifica_tamanho_listas(self, *listas: list):
        """Retorna 1 se todas as listas tem o mesmo tamanho

        Raises:
            Exception: Lista vazia
            Exception: Mesmo tamanho

        Returns:
            int: 1 if todos tamanhos iguais
                 2 if tamanhos diferentes
        """
        lista = []
        for n in listas:
            n = len(n)
            lista.append(n)
        lista = set(lista)
        if len(lista) > 1:
            logger.error(f"As listas tem tamanhos diferentes")
            return 0
        elif len(lista) == 0:
            logger.error(f"As listas estão vazias")
            return 0
        elif len(lista) == 1:
            logger.info(f"As listas tem o mesmo tamanho")
            return 1