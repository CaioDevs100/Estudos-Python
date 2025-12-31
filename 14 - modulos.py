
# Importa o módulo random para gerar números aleatórios, esse e um módulo padrão do Python
import random 
# Importa o módulo operacoes.py que contém funções matemáticas personalizadas 
import operacoes 

# Função para exibir o menu de opções ao usuário
def exibir_menu():
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Número aleatório")
    print("0. Sair")    

def definir_valores():
    a = float(input("Digite o primeiro número: ")) # Solicita ao usuário o primeiro número e converte para float
    b = float(input("Digite o segundo número: ")) # Solicita ao usuário o segundo número e converte para float
    return [a, b] # Retorna os valores como uma lista

while True: # Loop infinito para o menu
    exibir_menu()
    escolha = input("Escolha uma operação (0 para sair): ") # Solicita ao usuário que escolha uma operação
    
    # Verifica se o usuário escolheu sair
    if escolha == '0': 
        print("Saindo...")
        # Sai do loop e termina o programa (quebra o while)
        break 

    # Verifica se o usuário escolheu soma
    if escolha == '1': 
        # Obtém os valores do usuário
        a, b = definir_valores()
        # Chama a função soma do módulo operacoes 
        resultado = operacoes.soma(a, b) 
        # Imprime o resultado da soma
        print(f"Resultado: {resultado}") 
    
    # Verifica se o usuário escolheu subtração
    elif escolha == '2': 
        # Obtém os valores do usuário
        a, b = definir_valores() 
        # Chama a função subtracao do módulo operacoes
        resultado = operacoes.subtracao(a, b)
        # Imprime o resultado da subtração
        print(f"Resultado: {resultado}") 
    
    # Verifica se o usuário escolheu multiplicação
    elif escolha == '3': 
        # Obtém os valores do usuário
        a, b = definir_valores() 
        # Chama a função multiplicacao do módulo operacoes
        resultado = operacoes.multiplicacao(a, b) 
        # Imprime o resultado da multiplicação
        print(f"Resultado: {resultado}")
    
    # Verifica se o usuário escolheu divisão
    elif escolha == '4':
        # Obtém os valores do usuário
        a, b = definir_valores()
        # Verifica se o divisor não é zero
        if b != 0:
            # Chama a função divisao do módulo operacoes
            resultado = operacoes.divisao(a, b)
            # Imprime o resultado da divisão
            print(f"Resultado: {resultado}")
        # Se o divisor for zero, exibe uma mensagem de erro
        else:
            print("Erro: Divisão por zero não é permitida.")
    # Verifica se o usuário escolheu número aleatório
    elif escolha == '5':
        # Obtém os valores do usuário
        a, b = definir_valores()
        # Gera um número aleatório entre a e b
        resultado = random.uniform(a, b)
        # Imprime o número aleatório gerado
        print("Resultado: ", resultado)
    # Se a opção escolhida for inválida
    else:
        print("Opção inválida. Tente novamente.")


