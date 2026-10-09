import os
os.system('cls')

QUANTIDADE = 2

for i in range(QUANTIDADE):
    while True:
        nota_um = float(input('Digite sua primeira nota: '))
        nota_dois = float(input('Digite sua segunda nota: '))
        media = (nota_um + nota_dois) / 2
        if media < 0 or media > 10:
            print('Nota invalida. ')
        else:
            print(f'Sua media é: {media}')
            break
        break
