# Tabuada de um número fornecido pelo usuário

# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Exibe a tabuada 
print(f"Tabuada do {numero}:")

# Loop para calcular e exibir a tabuada, range siginifica "intervalo"
for i in range(1, 11): # Vai de 1 até 10 porque sempre o último número é excluído e i é o contador
    # Calcula o resultado da multiplicação 
    resultado = numero * i
    # Exibe o resultado formatado
    print(f"{numero} x {i} = {resultado}") 

