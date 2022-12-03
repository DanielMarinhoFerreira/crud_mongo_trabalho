import pandas as pd
from model.servidor import Servidor
from conexion.mongo_queries import MongoQueries

class Controller_Servidor:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_servidor(self) -> Servidor:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuario o novo nome
        servidor = input("ID Servidor (Novo): ")

        if self.verifica_existencia_servidor(servidor):
            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")
            # Insere e persiste o novo Servidor
            self.mongo.db["servidor"].insert_one({"id_servidor": servidor, "nome": nome})
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_servidor = self.recupera_servidor(servidor)
            # Cria um novo objeto Servidor
            novo_servidor = Servidor(df_servidor.servidor.values[0], df_servidor.nome.values[0])
            # Exibe os atributos do novo servidor
            print(novo_servidor.to_string())
            self.mongo.close()
            # Retorna o objeto novo_servidor para utilização posterior, caso necessário
            return novo_servidor
        else:
            self.mongo.close()
            print(f"O Servidor {servidor} já está cadastrado.")
            return None

    def atualizar_servidor(self) -> Servidor:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do servidor a ser alterado
        servidor = input("ID do servidor que deseja alterar o nome: ")

        # Verifica se o servidor existe na base de dados
        if not self.verifica_existencia_servidor(servidor):
            # Solicita a nova descrição do servidor
            novo_nome = input("Nome (Novo): ")
            # Atualiza o nome do servidor existente
            self.mongo.db["servidor"].update_one({"id_servidor": f"{servidor}"}, {"$set": {"nome": novo_nome}})
            # Recupera os dados do novo servidor criado transformando em um DataFrame
            df_servidor = self.recupera_servidor(servidor)
            # Cria um novo objeto servidor
            servidor_atualizado = Servidor(df_servidor.servidor.values[0], df_servidor.nome.values[0])
            # Exibe os atributos do novo servidor
            print(servidor_atualizado.to_string())
            self.mongo.close()
            # Retorna o objeto servidor_atualizado para utilização posterior, caso necessário
            return servidor_atualizado
        else:
            self.mongo.close()
            print(f"O Servidor {servidor} não existe.")
            return None

    def excluir_servidor(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o ID do Servidor a ser alterado
        servidor = input("ID do Servidor que irá excluir: ")

        # Verifica se o servidor existe na base de dados
        if not self.verifica_existencia_servidor(servidor):            
            # Recupera os dados do novo servidor criado transformando em um DataFrame
            df_servidor = self.recupera_servidor(servidor)
            # Revome o servidor da tabela
            self.mongo.db["servidor"].delete_one({"id_servidor":f"{servidor}"})
            # Cria um novo objeto servidor para informar que foi removido
            servidor_excluido = Servidor(df_servidor.servidor.values[0], df_servidor.nome.values[0])
            self.mongo.close()
            # Exibe os atributos do servidor excluído
            print("Servidor Removido com Sucesso!")
            print(servidor_excluido.to_string())
        else:
            self.mongo.close()
            print(f"O SERVIDOR {servidor} não existe.")

    def verifica_existencia_servidor(self, id_servidor:str=None, external:bool=False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_servidor = pd.DataFrame(self.mongo.db["servidor"].find({"servidor":f"{id_servidor}"}, {"id_conta": 1, "nome": 1, "_id": 0})) #verificar 

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_servidor.empty

    def recupera_servidor(self, id_servidor:str=None, external:bool=False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_servidor = pd.DataFrame(list(self.mongo.db["servidor"].find({"id_servidor":f"{id_servidor}"}, {"id_conta": 1, "nome": 1, "_id": 0})))
        
        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_servidor