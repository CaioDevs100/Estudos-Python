# Estrutura de Dados - Sets

# Sets são coleções não ordenadas de elementos únicos. Eles são definidos usando chaves {}.
# Tentando adicionar elementos duplicados em um set, eles serão ignorados.
usuarios = {"maria", "ana", "ana"}
usuarios.add("joao")
print(usuarios)

# Verifica se um usuário está cadastrado no set
usuario_digitado = input("Digite o nome do usuário: ")
if usuario_digitado in usuarios: 
    print("Usuário cadastrado")
else:
    print("Usuário não cadastrado")

# Criando outro set de usuários
novos_usuarios = {"pedro", "paulo", "maria"}

print(usuarios)
print(novos_usuarios)

# União de sets - une os dois sets, eliminando duplicatas
todos_usuarios = usuarios.union(novos_usuarios)
print(F"união:{todos_usuarios}")

# Interseção de sets - retorna apenas os elementos que estão em ambos os sets
usuarios_comuns = usuarios.intersection(novos_usuarios)
print(f"interseção: {usuarios_comuns}")

# Diferença de sets - retorna os elementos que estão no primeiro set, mas não no segundo
usuarios_diferentes = usuarios.difference(novos_usuarios)
print(f"diferença: {usuarios_diferentes}")




