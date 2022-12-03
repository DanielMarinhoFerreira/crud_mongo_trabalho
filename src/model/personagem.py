class Personagem:
    def __init__(self, id_personagem:str = None, self.id_conta:str = None, nome:str = None, nivel:int = None, classe:str = None):
        self.set_id_personagem(id_personagem)
        self.set_id_conta(id_conta)
        self.set_nome(nome)
        self.set_nivel(nivel)
        self.set_classe(classe)

    def set_id_personagem(self, id_personagem: str):
        self.id_personagem = id_personagem

    def set_id_conta(self, id_conta):
        self.id_conta = id_conta
    
    def set_nome(self, nome: str):
        self.nome = nome

    def set_nivel(self, nivel:int):
        self.nivel = nivel

    def set_classe(self, classe: str):
        self.classe = classe

    def get_id_personagem(self) -> str:
        return self.id_personagem

    def get_id_conta(self) -> str:
        return self.id_conta

    def get_nome(self) -> str:
        return self.nome

    def get_nivel(self) -> int:
        return self.nivel
    
    def get_classe(self) -> str:
        return self.classe


    def to_string(self) -> str:
        return f"id_personagem: {self.get_id_personagem()} | id_conta: {self.get_id_conta()} | nome: {self.get_nomes()} | nivel: {self.get_nivel()} | classe: {self.get_classe()}"


