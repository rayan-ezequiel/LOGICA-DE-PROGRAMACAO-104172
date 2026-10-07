import os
os.system('cls')

soma = 0.0

quantidade_de_notas = 0

nota = float(input(f'Digite sua nota {quantidade_de_notas + 1}º nota: '))
soma += nota
quantidade_de_notas += 1

while True:
    pergunta = input('Você deseja adicionar mais uma nota ? ').upper()

    if pergunta == 'S':
        nota = float(input(f'Digite sua {quantidade_de_notas + 1}º nota: '))
        soma += nota
        quantidade_de_notas += 1
    elif pergunta == 'N':
        media = soma / quantidade_de_notas
        print(f'Sua média é: {media}')