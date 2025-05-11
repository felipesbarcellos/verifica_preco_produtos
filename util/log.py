from loguru import logger

class Log:
    
    def __init__(self):
        ...
        
    def preco_produto_localizado(self, preco) -> None:
        logger.info("O software localizou o preço")
        logger.info(f"O preço do produto é: {preco}")
        
    def nome_produto_localizado(self, nome) -> None:
        logger.info("O software localizou o nome do produto")
        logger.info(f"O nome do produto é: {nome}")