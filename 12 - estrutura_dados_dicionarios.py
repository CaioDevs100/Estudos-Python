# Estrutura de Dados - Dicionários

# Dicionários são coleções de pares chave-valor. Eles são definidos usando chaves {}
# Cada chave deve ser única dentro do dicionário
cliente = {
    'nome': 'João Silva',
    'cidade': "São Roque",
    "ano_nascimento": 1985,
    "ativo": True
}
print(cliente["nome"]) # Acessando valor pela chave

cliente["ano_nascimento"] = 2000 # Atualizando valor

print(cliente)

del cliente["cidade"] # Removendo a chave-valor
print(cliente)

# Verificando se uma chave existe no dicionário
if "ano_nascimento" in cliente: 
    print(f"o cliente nasceu em: {cliente['ano_nascimento']}")
else:
    print("Não existe a chave.")


# Iterando sobre chaves e valores do dicionário
print(f"lista de valores:")
for valor in cliente.values(): # Iterando sobre os valores
    print(valor)

print(f"lista de chaves:")
for chave, valor in cliente.items(): # Iterando sobre as chaves
    print(chave)