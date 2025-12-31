# Estrutura de Dados Tupla 

# Tuplas são estruturas de dados imutáveis, ou seja, não podem ser alteradas após a criação. Elas são definidas usando parênteses ().
#            1          2       3         4
cores = ('vermelho', 'verde', 'azul', 'amarelo')
print(f"Meu carro é {cores[2]}")

# Tamanho da tupla, len retorna o número de elementos na tupla 
quantidade = len(cores)
print(f"Eu tenho {quantidade} cores disponíveis.")

# Verifica se uma cor está na tupla e conta quantas vezes ela aparece
cor = input("Digite uma cor: ")
if cor in cores:
    quantidade_cor = cores.count(cor)
    print(f"Temos {quantidade_cor} tipo de {cor}")
else:
    print(f"A cor {cor} não está disponível.")

# Desempacotamento de tuplas 
aluno = ('Ana', 21, 5)
nome, nota1, nota2 = aluno
media = (nota1 + nota2) / 2

print(f"O aluno {nome} com as nota {nota1} e {nota2} está com a média {media}")