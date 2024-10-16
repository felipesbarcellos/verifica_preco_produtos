from datetime import datetime

class Tempo():
    def __init__(self) -> None:
        self.hoje: str = self.get_data_hoje_str()
        pass

    def get_data_hoje_str(self) -> str:
        hoje = datetime.today()
        dia = hoje.day
        mes = hoje.month
        ano = hoje.year

        data = f"{dia}/{mes}/{ano}"
        return data
    
    def string_to_datetime(self, ano:str = "01/01/2010") -> datetime:
        dia = int(ano.split("/")[0])
        mes = int(ano.split("/")[1])
        ano = int(ano.split("/")[2])
        return datetime(day=dia, month=mes, year=ano)