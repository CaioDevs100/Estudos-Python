# Entrada e saída de dados em Python


# Solicitando ao usuário que insira seu nome e idade
nome = input("Digite seu nome: ")
# covertendo a entrada de idade para inteiro
idade = int(input("Digite sua idade: "))

# Calculando o ano de nascimento
ano = 2024 - idade

# Criando uma mensagem formatada com os dados fornecidos
mensagem = f"Olá, seu nome é {nome} e você nasceu em {ano}."

# Exibindo a mensagem na tela
print(mensagem)