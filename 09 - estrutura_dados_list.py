# Estrutura de Dados - Listas em Python
# Listas são coleções ordenadas e mutáveis que permitem armazenar múltiplos valores em uma única variável.

# Criando uma lista
#          0       1        2         3     
nomes = ["Ana", "Bruno", "Carlos", "Diana"] 
print(f"Lista original: {nomes}")

# Acessando elementos da lista
for cont in range(1, 3): 
    novo_nome = input(f"Digite o nome {cont}: ")
    nomes.append(novo_nome)
print(f"Lista adicionando 2 nomes: {nomes}")

# Adicionando elementos dinamicamente com loop
resp = "s"
while resp == "s":
    novo_nome = input(f"Digite o nome: ")
    nomes.append(novo_nome)
    resp = input("Deseja adicionar mais um nome? (s/n): ")
print(f"Lista adicionando n nomes: {nomes}")

# listando elementos pela posição
print(nomes[0])  # Primeiro elemento

# Removendo o ultimo elemento da lista
nomes.pop()
print(f"Removendo o último nome: {nomes}")

# Removendo um elemento específico da lista
nomes.remove("Bruno")
print(f"Removendo um elemento: {nomes}")

# verificando a existência de um elemento na lista
nome_pesquisado = input("Digite um nome para pesquisar na lista: ")
if nome_pesquisado in nomes:
    print(f"{nome_pesquisado} encontrado na lista!")
else:
    print(f"{nome_pesquisado} não encontrado na lista.")
