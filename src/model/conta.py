class Conta:
    def __init__(self.id_conta:str = None , self.id_servidor:str = None, self.nome:str = None, self.email:str = None):
        self.set_id_conta(id_conta)
        self.set_id_servidor(id_servidor)
        self.set_nome(nome)
        self.set_email(email)

    def set_id_conta(self, id_conta):
        self.id_conta = id_conta

    def set_id_servidor(self, id_servidor: str):
        self.id_servidor = id_servidor

    def set_nome(self, nome: str):
        self.nome = nome

    def set_email(self, email: str):
        self.email = email

    def get_id_conta(self) -> str:
        return self.id_conta

    def get_id_servidor(self) -> str:
        return self.id_servidor

    def get_nome(self) -> str:
        return self.nome

    def get_email(self) -> str:
        return self.email

    def to_string(self) -> str:
        return f"id_conta: {self.get_id_conta()} | id_servidor: {self.get_id_servidor()} | nome: {self.get_nomes()} | email: {self.get_email()}"
