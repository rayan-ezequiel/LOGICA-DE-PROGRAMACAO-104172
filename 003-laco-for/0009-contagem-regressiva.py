import time
import os
os.system('cls')

print('Contagem Regressiva')

numero = int(input('Digite o número: '))

for i in range(numero, -1, -1):
    time.sleep(1)
    print(i)
