from datetime import datetime

class Hoje():
    def __init__(self) -> None:
        self.hoje: str = self.get_data_hoje()
        pass

    def __repr__(self) -> str:
        return self.hoje

    def get_data_hoje(self) -> str:
        hoje = datetime.today()
        dia = hoje.day
        mes = hoje.month
        ano = hoje.year

        data = f"{dia}/{mes}/{ano}"
        return data