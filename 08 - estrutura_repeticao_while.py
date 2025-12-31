# Estrutura de repetição while

# Solicita ao usuário que digite a senha 
senha = input("Digite a senha: ")
senha_correta = "123"

# Enquanto a senha digitada for diferente (!) de senha_correta, continue pedindo a senha 
while senha != senha_correta:
    print("Senha incorreta! Tente novamente!!!")
    senha = input("Digite a senha: ")

print("Senha correta! Acesso permitido!")