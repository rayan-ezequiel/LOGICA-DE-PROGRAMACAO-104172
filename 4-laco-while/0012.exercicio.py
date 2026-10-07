import os
os.system('cls')

soma = 0.0
quantidade_de_notas = 0

while True:
    nota = float(input(f'Digite sua nota {quantidade_de_notas + 1}º nota: '))
    if nota > 0:
        soma += nota
        quantidade_de_notas += 1
    elif nota < 0:
        media = soma / quantidade_de_notas
        print(f'Sua média é: {media}')
        break