from conexion.mongo_queries import MongoQueries
import pandas as pd
from pymongo import ASCENDING, DESCENDING

class Relatorio:
    def __init__(self):
        pass

    def get_relatorio_servidor(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["servidor"].find({}, 
                                                 {"id_servidor": 1, 
                                                  "nome": 1, 
                                                  "_id": 0
                                                 }).sort("id_servidor", ASCENDING)
        df_cliente = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_cliente)
        input("Pressione Enter para Sair do Relatório de Servidores")

    def get_relatorio_conta(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["conta"].find({}, 
                                                     {"id_conta": 1, 
                                                      "id_servidor": 1, 
                                                      "nome": 1, 
                                                      "email":1,
                                                      "_id": 0
                                                     }).sort("nome", ASCENDING)
        df_fornecedor = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_fornecedor)        
        input("Pressione Enter para Sair do Relatório de Fornecedores")

    def get_relatorio_personagem(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["clientes"].find({}, 
                                                 {"id_personagem": 1, 
                                                  "id_conta": 1, 
                                                  "nome": 1, 
                                                  "nivel": 1, 
                                                  "classe": 1, 
                                                  "_id": 0
                                                 }).sort("nome", ASCENDING)
        df_cliente = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_cliente)
        input("Pressione Enter para Sair do Relatório de Clientes")