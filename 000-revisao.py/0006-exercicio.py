import os
import time 
os.system('cls')


print('Mostrando o cubo de um número')

numero = int(input('Digite um número: '))

for i in range(1, numero + 1):
    cubo = i ** 3
    print(f'o número atual é: {i} e o cubo é {cubo}')
    time.sleep(1)

