# list 
valores = [100, 30, 45, 33, 99]

# função 
def mensagem():
    print("Olá! Esta é uma mensagem de função.")

def calcular_desconto(preco):
    preco_final = preco * 0.9  
    return preco_final

def soma (a, b):
    return a + b

mensagem()

valor_pagar = calcular_desconto(100)
print(f"{valor_pagar:.2f}") # :.2f e a qauntidade de casas decimais

total = soma(4, 90)
print (total)

print("### Valores com desconto ###")
for valor in valores:
    valor_desconto = calcular_desconto(valor)
    print(f"{valor_desconto:.2f}")