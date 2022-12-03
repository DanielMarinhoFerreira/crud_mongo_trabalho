class Servidor:
    def __init__(self, id_servidor:str = None, nome:str = None):
        self.set_id_servidor(id_servidor)
        self.set_nome(nome)

    def set_id_servidor(self, id_servidor: str):
        self.id_servidor = id_servidor

    def set_nome(self, nome):
        self.nome = nome

    def get_id_servidor(self) -> str:
        return self.id_servidor
                
    def get_nome(self) -> str:
        return self.nome

    def to_string(self) -> str:
        return f"id_servidor: {self.get_id_servidor()} | nome: {self.get_nomes()}"
