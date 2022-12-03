from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_servidor import Controller_Servidor
from controller.controller_conta import Controller_Conta
from controller.controller_personagem import Controller_Personagem

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_servidor = Controller_Servidor()
ctrl_conta = Controller_Conta()
ctrl_personagem = Controller_Personagem()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_servidor()            
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_conta()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_personagem()


def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_servidor = ctrl_servidor.inserir_servidor()
    elif opcao_inserir == 2:
        novo_conta = ctrl_conta.inserir_conta()
    elif opcao_inserir == 3:
        novo_personagem = ctrl_personagem.inserir_personagem()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_servidor()
        produto_atualizado = ctrl_servidor.atualizar_servidor()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_conta()
        conta_atualizado = ctrl_conta.atualizar_conta()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_personagem()
        personagem_atualizado = ctrl_personagem.atualizar_personagem()

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_servidor()
        ctrl_servidor.excluir_servidor()
    elif opcao_excluir == 2:                
        relatorio.get_relatorio_conta()
        ctrl_conta.excluir_conta()
    elif opcao_excluir == 3:                
        relatorio.get_relatorio_personagem()
        ctrl_personagem.excluir_personagem()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-4]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()