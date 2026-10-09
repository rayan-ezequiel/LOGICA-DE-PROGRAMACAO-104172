import os
os.system('cls')

numero = int(input('Digite um numero: '))
print('Tabuada')
print('\nMultiplicacao')
for i in range (1, 11):
    print(f'{numero} x {i} = {numero * i}')
print('\nSoma')
for i in range (1, 11):
    print(f'{numero} + {i} = {numero + i}')
print('\nSubtracao')
for i in range (1, 11):
    print(f'{numero} - {i} = {numero - i}')
print('\nDivisao')
for i in range (1, 11):
    print(f'{numero} / {i} = {numero / i:.2f}')