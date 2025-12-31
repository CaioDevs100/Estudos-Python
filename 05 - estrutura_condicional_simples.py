# Estrutura Condicional Simples

# Número de horas trabalhadas 
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
# Valor pago por hora
valor_hora = float(input("Digite o valor pago por hora: "))

# Verifica se o funcionário tem direito ao bônus
if (horas_trabalhadas >= 100):
    bonus = 500
# Caso contrário, não há bônus    
else:
    bonus = 0

# Cálculo do salário total
salario = horas_trabalhadas * valor_hora + bonus
# Exibe o salário total
print(f"O salário total é: R$ {salario}")