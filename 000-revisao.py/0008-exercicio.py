import os
import time
os.system('cls')

lista1 = [10, 20, 10, 30, 10, 40, 50]
alvo = 10
contagem = 0

for item in lista1:
    if item == alvo:
        contagem += 1
print(f'O número {alvo}, aparece {contagem} vezes.')