import pandas as pd
from model.personagem import Personagem
from conexion.mongo_queries import MongoQueries

class Controller_Personagem:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_personagem(self) -> Personagem:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()
        # Solicita ao usuario uma conta existente
        conta = input("Qual o ID da conta em que personagem será criado: ")

        if not self.verifica_existencia_servidor(conta):
            # Solicita ao usuario o novo id
            personagem = input("ID Personagem (Novo): ")

            if self.verifica_existencia_servidor(personagem):
                # Solicita ao usuario o novo nome
                nome = input("Nome (Novo): ")
                # Solicita ao usuario o novo nível
                nivel = input("Nível (Novo): ")
                # Solicita ao usuario a nova classe
                classe = input("Classe (Novo): ")
                # Insere e persiste o novo Personagem
                self.mongo.db["personagem"].insert_one({"id_personagem": personagem, "id_conta": conta, "nome": nome, "nivel": nivel, "classe": classe})
                # Recupera os dados do novo cliente criado transformando em um DataFrame
                df_personagem = self.recupera_personagem(personagem)
                # Cria um novo objeto Personagem
                novo_personagem = Personagem(df_personagem.personagem.values[0], df_personagem.conta.values[0], df_personagem.nome.values[0], df_personagem.nivel.values[0], df_personagem.classe.values[0])
                # Exibe os atributos do novo personagem
                print(novo_personagem.to_string())
                self.mongo.close()
                # Retorna o objeto novo_personagem para utilização posterior, caso necessário
                return novo_personagem
            else:
                self.mongo.close()
                print(f"O Personagem {personagem} já está cadastrado.")
                return None
        else:
            self.mongo.close()
            print(f"A Conta {conta} não existe.")
            return None

    def atualizar_personagem(self) -> Personagem:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do personagem a ser alterado
        personagem = input("ID do personagem que deseja alterar o nome: ")

        # Verifica se o personagem existe na base de dados
        if not self.verifica_existencia_personagem(personagem):
            # Solicita a nova descrição do personagem
            novo_nome = input("Nome (Novo): ")
            # Solicita ao usuario o novo nível
            novo_nivel = input("Nível (Novo): ")
            # Solicita ao usuario a nova classe
            nova_classe = input("Classe (Novo): ")
            # Atualiza o nome do personagem existente
            self.mongo.db["personagem"].update_one({"id_personagem": f"{personagem}"}, {"$set": {"nome": novo_nome,
                                                                                                "nivel": int(novo_nivel),
                                                                                                "classe": nova_classe}})
            # Recupera os dados do novo personagem criado transformando em um DataFrame
            df_personagem = self.recupera_personagem(personagem)
            # Cria um novo objeto personagem
            personagem_atualizado = Personagem(df_personagem.personagem.values[0], df_personagem.conta.values[0], df_personagem.nome.values[0], df_personagem.nivel.values[0], df_personagem.classe.values[0])
            # Exibe os atributos do novo personagem
            print(personagem_atualizado.to_string())
            self.mongo.close()
            # Retorna o objeto personagem_atualizado para utilização posterior, caso necessário
            return personagem_atualizado
        else:
            self.mongo.close()
            print(f"O personagem {personagem} não existe.")
            return None

    def excluir_personagem(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o ID do Personagem a ser alterado
        personagem = input("ID do Personagem que irá excluir: ")

        # Verifica se o personagem existe na base de dados
        if not self.verifica_existencia_personagem(personagem):            
            # Recupera os dados do novo personagem criado transformando em um DataFrame
            df_personagem = self.recupera_personagem(personagem)
            # Revome o personagem da tabela
            self.mongo.db["personagem"].delete_one({"id_personagem":f"{personagem}"})
            # Cria um novo objeto personagem para informar que foi removido
            personagem_excluido = Personagem(df_personagem.personagem.values[0], df_personagem.conta.values[0], df_personagem.nome.values[0], df_personagem.nivel.values[0], df_personagem.classe.values[0])
            self.mongo.close()
            # Exibe os atributos do personagem excluído
            print("personagem Removido com Sucesso!")
            print(personagem_excluido.to_string())
        else:
            self.mongo.close()
            print(f"O personagem {personagem} não existe.")

    def verifica_existencia_personagem(self, id_personagem:str=None, external:bool=False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_personagem = pd.DataFrame(self.mongo.db["personagem"].find({"personagem":f"{id_personagem}"}, {"id_conta": 1, "nome": 1, "nivel": 1, "classe": 1, "_id": 0}))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_personagem.empty

    def recupera_personagem(self, id_personagem:str=None, external:bool=False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_personagem = pd.DataFrame(list(self.mongo.db["personagem"].find({"id_personagem":f"{id_personagem}"}, {"id_conta": 1, "nome": 1, "nivel": 1, "classe": 1, "_id": 0})))
        
        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_personagem