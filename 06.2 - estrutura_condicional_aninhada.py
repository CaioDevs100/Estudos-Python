# Estrutura condicional aninhada

# Solicita ao usuário a nota e a frequência do aluno
nota = float(input("Digite a nota do aluno: "))
frequencia = int(input("Digite a frequência do aluno: "))

# Determina a situação do aluno com base na nota e frequência
if nota >= 5 and frequencia >= 75: 
    situacao = "Aprovado"
elif nota >= 5 or frequencia >= 75: 
    situacao = "na recuperação"
else:
    situacao = "Reprovado"

print(f"O aluno está: {situacao}!")