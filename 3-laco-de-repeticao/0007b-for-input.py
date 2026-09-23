import os
import time
os.system('cls')

numeros1 = 0.0

for i in range(1, 6):
    numeros = float(input(f'Digite seu número {i}º: '))
    numeros1 += numeros
    time.sleep(1)
print(f'A soma de todos os números é: {numeros1}')
