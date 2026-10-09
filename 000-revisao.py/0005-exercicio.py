import os
import time
os.system('cls')

numero = int(input('Digite um número: '))
for i in range(1, 11):
    tabuada = numero * i
    time.sleep(1)
    print(f'{numero} x {i} = {tabuada}')