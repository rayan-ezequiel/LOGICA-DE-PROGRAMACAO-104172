import time
import os
os.system('cls')

soma = 0
QUANTIDADE = 10

print('ACUMULANDO VALORES EM UMA VARIAVEL')

print(f'\nValor inicial da variavel é: {soma}')

for i in range(QUANTIDADE):
    soma += int(input('Digite um número para somar: '))
    print(f'\nValor temporario: {soma}')
print(f'\nValor final da variavel: {soma}')
