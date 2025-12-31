# Pequeno projeto para consolidar o aprendizado

# Importa o módulo os para operações do sistema
import os 
# Importa a função ler_cidades do módulo cidades
from cidades import ler_cidades

# Função para limpar a tela do terminal
def limpar_tela():
    # Comando para limpar a tela, dependendo do sistema operacional para Windows ou Unix-based 
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para pausar a execução até que o usuário pressione Enter
def pausar():
    # Aguarda o usuário pressionar Enter
    input("Pressione Enter para continuar...")

# Função para exibir o menu de opções
def exibir_menu():
    print("===== Menu =====")
    print("1. Listar cidades")
    print("2. Adicionar cidade")
    print("3. Atualizar cidade")
    print("4. Buscar cidade")
    print("5. Excluir cidade")
    print("0. Sair")

# Função para processar a opção escolhida pelo usuário
def processar_opcao(opcao):
    # Se a opção for 1, listar as cidades
    if opcao == '1':
        # Chama a função ler_cidades do módulo cidades
        cidades = ler_cidades()
        # Exibe as cidades lidas
        for cidade in cidades:
            # Imprime cada cidade na tela
            print(cidade)

# Função principal para executar o sistema
def executar_sistema():
    # Loop infinito para manter o sistema em execução até o usuário decidir sair
    exibir_menu()
    # Solicita ao usuário que escolha uma opção
    opcao = input("Escolha uma opção: ")
    # Limpa a tela antes de processar a opção
    limpar_tela()
    # Processa a opção escolhida pelo usuário
    processar_opcao(opcao)
    # Pausa a execução para que o usuário possa ver o resultado
    pausar()
    # Se a opção for 0, sai do sistema
    executar_sistema()
# Inicia a execução do sistema
executar_sistema()

