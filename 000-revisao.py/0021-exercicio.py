import os
os.system('cls' if os.name == 'nt' else 'clear')


# Folha de Pagamento com Desconto VETORES FOR CÁLCULOS
# Receba o salário bruto de 5 funcionários e armazene em um vetor. Para cada salário, aplique 10% de salario_com_desconto
# se for maior que R$ 2.500,00 ou 5% se for menor/igual. Exiba a lista com os salários líquidos e o valor total
# gasto pela empresa

salarios_bruto = []
salarios_liquidos = []

for i in range(5):
    salario = float(input(f"Digite salário {i + 1}º funcionário: R$ "))
    salarios_bruto.append(salario)
    if salario > 2500:
        salario_com_desconto = salario - (salario * 0.10)
        salarios_liquidos.append(salario_com_desconto)
    else:
        salario_com_desconto = salario - (salario * 0.05)
        salarios_liquidos.append(salario_com_desconto)


salarios_formatados = ", ".join([f"R$ {s:.2f}" for s in salarios_liquidos])
print(f'Salários líquidos: R$ {salarios_formatados}\nGasto pela empresa: R$ {sum(salarios_bruto)}')
