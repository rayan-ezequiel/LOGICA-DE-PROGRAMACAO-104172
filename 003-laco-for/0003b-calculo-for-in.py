import os
os.system('cls')

numero = int(input('Digite um numero: '))
op = input('Digite a operação: ')
print('Tabuada')
match op:
    case '*':
        print('\nMultiplicacao')
        for i in range (1, 11):
            print(f'{numero} x {i} = {numero * i}')
    case '+':
        print('\nSoma')
        for i in range (1, 11):
            print(f'{numero} + {i} = {numero + i}')
    case '-':
        print('\nSubtracao')
        for i in range (1, 11):
            print(f'{numero} - {i} = {numero - i}')
    case '/':
        print('\nDivisao')
        for i in range (1, 11):
            print(f'{numero} / {i} = {numero / i:.2f}')