# Estrutura Condicional Aninhada

# Solicita ao usuário o número de anos de experiência
anos_experiencia = int(input("Digite o número de anos de experiência: "))

# Determina o nível do profissional com base nos anos de experiência
if anos_experiencia == 0:
    nivel = "estagiário"
elif anos_experiencia <= 2:
    nivel = "júnior"
elif anos_experiencia <= 5:
    nivel = "pleno"
else:
    nivel = "sênior"

print(f"O nível do profissional é: {nivel}")