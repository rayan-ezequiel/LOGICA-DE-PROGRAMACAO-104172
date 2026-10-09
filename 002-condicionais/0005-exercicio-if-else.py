import os
os.system('cls')

numero1 = float(input('Digite o primeiro numero1: '))
numero2 = float(input('Digite o segundo numero2: '))

media = numero1 + numero2 / 2
soma = (numero1 + numero2)
produto = (numero1 * numero2)


print('\n A  media é: ', media, '\n a soma é: ', soma, '\n o produto é: ', produto)


if numero1 > numero2:
    print(numero1, 'é o maior numero', '\n',numero2, 'é o menor numero')
else: print(numero2, 'é o maior numero', numero1, 'é o menor numero')

