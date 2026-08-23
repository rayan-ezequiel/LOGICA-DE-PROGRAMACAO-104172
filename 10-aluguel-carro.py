import os
os.system('cls')

#Objetivo: Escreva um programa que pergunte a quantidade 
# de quilômetros (Km) percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço total a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado

print('= Aluguel de Carros =')

dias = float(input('Por quantos dias você rodou ? '))
quilometros = float(input('Quantos quilômetros rodou ? '))


aluguel = (dias * 60)
taxa_km = (quilometros * 0.15) 
soma = (aluguel + taxa_km)
print('Você rodou por ', dias, 'dias e pecorreu', quilometros, 'km')
print('Foi gasto R$', aluguel, 'do aluguel e R$', taxa_km, 'dos quilometros rodados!!')
print('o total deu: R$', soma)
print('VOLTE SEMPRE <3')
