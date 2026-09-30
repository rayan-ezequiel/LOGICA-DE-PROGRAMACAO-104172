import os
os.system('cls')

soma = 0

QUANTIDADE = 2

for i in range(QUANTIDADE):
    while True:
        nota = float(input('Digite sua nota: '))
        if nota < 0 and nota < 10:
            nota + soma
            print('Nota inválida.')
        else:
            media = soma /2
            print(f'Sua média é: {media}')
            break
        break
