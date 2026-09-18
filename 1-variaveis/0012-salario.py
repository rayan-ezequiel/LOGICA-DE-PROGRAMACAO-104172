import os
os.system('cls')

print('Salarios minimos')

salario_atual = float(input('Digite o seu salario atual: '))
salario_mensal = float(1621.00)
divisao = salario_atual / salario_mensal

print('a quantidade de salarios minimos que voce recebe é: ', f"{divisao:.0f}")