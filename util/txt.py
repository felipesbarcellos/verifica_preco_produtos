from util.constants import PRECOS_PATH, LINKS_PATH


class Txt:
    """Representa os arquivos de texto dentro 
    """    
    def __init__(self, path:str):
        """Instancia a classe, recebendo o caminho como texto

        Args:
            path (str): _description_
        """
        self.path = path
        self.linhas: list[str] = self.get_linhas()
        pass

    def get_linhas(self) -> list[str]:
        try:
            """Retorna todas as linhas do arquivo txt
            """        
            with open(self.path, mode='r', encoding='utf-8') as f:
                linhas: list["str"] = f.readlines()
                return linhas
        except Exception as e:
            # TODO Instancia de Log registra no 
            # arquivo de log tipo da exceção
            ... #XXX Implementar após abstrair o sistema de logs

    def escrever(self, text: str | list[str]) -> None:
        """Escreve o texto no arquivo txt

        Args:
            text (str | list[str]): texto que
            será escrito no arquivo.txt
        """
        try:
            with open(self.path, mode='a', encoding='utf-8') as f:
                if isinstance(text, str): #Se o texto for string
                    f.write(f"{text}\n")
                elif isinstance(text, list):
                    f.writelines(linha + '\n' for linha in text)
        except IOError as e:
            ... #XXX Implementar após abstrair o sistema de logs
        
    def cria_arquivo(self):
        try:
            f = open(self.path, mode="x")
            f.close()
            # logger.debug(f"Arquivo {nome} criado com sucesso!")
        except FileExistsError:
            # logger.debug(f"O arquivo {nome} já existe")
            pass

class Precos(Txt):
    def __init__(self):
        super().__init__(path=PRECOS_PATH)

    def salvar_preco(self, titulo: str, preco: float, data: str):
        with open(PRECOS_PATH, mode="a", encoding="utf-8") as f:
            linhas = self.get_linhas()
            no_texto = None
            for linha in linhas:
                if (str(titulo) in linha) and (str(data) in linha):
                    no_texto = 1
                    break
                else:
                    no_texto = 0
            if not no_texto:
                f.write(f"{titulo} | {preco} | {data}\n")

class Links(Txt):
    def __init__(self):
        super().__init__(path=LINKS_PATH)

    