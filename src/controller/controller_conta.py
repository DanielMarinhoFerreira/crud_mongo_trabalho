import pandas as pd
import Controller_Servidor as cs
from model.conta import Conta
from conexion.mongo_queries import MongoQueries

class Controller_Conta:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_conta(self) -> Conta:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuario o novo nome
        conta = input("ID Conta (Novo): ")

        if self.verifica_existencia_conta(conta):
            # Solicita ao usuario o novo Servidor
            servidor = input("Servidor (Novo): ")
            # Verifica se o usuário está inserindo um servidor cadastrado
            while not cs.verifica_existencia_servidor(servidor):
                input("Esse servidor não existe!")
                servidor = input("Servidor (Novo): ")
                if cs.verifica_existencia_servidor(servidor):
                    break

            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")
            # Solicita ao usuario o novo email
            email = input("Email (Novo): ")
            # Insere e persiste o novo conta
            self.mongo.db["conta"].insert_one({"id_conta": conta, "id_servidor": servidor, "nome": nome, "email": email})
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_conta = self.recupera_conta(conta)
            # Cria um novo objeto conta
            nova_conta = conta(df_conta.conta.values[0], df_conta.nome.values[0])
            # Exibe os atributos do novo conta
            print(nova_conta.to_string())
            self.mongo.close()
            # Retorna o objeto nova_conta para utilização posterior, caso necessário
            return nova_conta
        else:
            self.mongo.close()
            print(f"A conta {conta} já está cadastrada.")
            return None

    def atualizar_conta(self) -> Conta:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do servidor a ser alterado
        conta = input("ID da conta que deseja alterar o nome: ")

        # Verifica se a conta existe na base de dados
        if not self.verifica_existencia_conta(conta):
            # Solicita ao usuario o novo Servidor
            novo_servidor = input("Servidor (Novo): ")

            # Verifica se o usuário está inserindo um servidor cadastrado
            while not cs.verifica_existencia_servidor(servidor):
                input("Esse servidor não existe!")
                novo_servidor = input("Servidor (Novo): ")
                if cs.verifica_existencia_servidor(novo_servidor):
                    break

            # Solicita ao usuario o novo nome
            novo_nome = input("Nome (Novo): ")
            # Solicita ao usuario o novo email
            novo_email = input("Email (Novo): ")
            # Atualiza o nome do conta existente
            self.mongo.db["conta"].update_one({"id_conta": f"{conta}"}, {"$set": {"sid_servidor": novo_servidor,
                                                                                    "nome": novo_nome,
                                                                                    "email": novo_email}})
            # Recupera os dados da nova conta criado transformando em um DataFrame
            df_conta = self.recupera_conta(conta)
            # Cria um novo objeto conta
            conta_atualizado = Conta(df_conta.conta.values[0], df_conta.servidor.values[0], df_conta.nome.values[0], df_conta.email.values[0])
            # Exibe os atributos da nova conta
            print(conta_atualizado.to_string())
            self.mongo.close()
            # Retorna o objeto conta_atualizado para utilização posterior, caso necessário
            return conta_atualizado
        else:
            self.mongo.close()
            print(f"A Conta {conta} não existe.")
            return None

    def excluir_conta(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o ID da conta a ser alterada
        conta = input("ID da conta que irá excluir: ")

        # Verifica se o conta existe na base de dados
        if not self.verifica_existencia_conta(conta):            
            # Recupera os dados do novo conta criado transformando em um DataFrame
            df_conta = self.recupera_conta(conta)
            # Revome o conta da tabela
            self.mongo.db["conta"].delete_one({"id_conta":f"{conta}"})
            # Cria um novo objeto conta para informar que foi removido
            conta_excluido = Conta(df_conta.conta.values[0], df_conta.servidor.values[0], df_conta.nome.values[0], df_conta.email.values[0])
            self.mongo.close()
            # Exibe os atributos do conta excluído
            print("Conta Removida com Sucesso!")
            print(conta_excluido.to_string())
        else:
            self.mongo.close()
            print(f"C Conta {conta} não existe.")

    def verifica_existencia_conta(self, id_conta:str=None, external:bool=False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_conta = pd.DataFrame(self.mongo.db["conta"].find({"conta":f"{id_conta}"}, {"id_servidor": 1, "nome": 1, "email": 1, "_id": 0}))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_conta.empty

    def recupera_conta(self, id_conta:str=None, external:bool=False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_conta = pd.DataFrame(list(self.mongo.db["conta"].find({"id_conta":f"{id_conta}"}, {"id_servidor": 1, "nome": 1, "email": 1, "_id": 0})))
        
        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_conta