import os
os.system('cls')

numero  = int(input('Digite um número: '))

for multiplicando in range(1, 11):
    tabuada = numero * multiplicando
    print(f'{numero} x {multiplicando} = {tabuada}')