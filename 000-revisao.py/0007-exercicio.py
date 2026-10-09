import os
import time
os.system('cls')

# O número deve ser divisível por cinco.
# Se o número for maior que 150, pule-o e passe para o próximo.
# Se o número for maior que 500, pare o loop inteiramente.
numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item > 500:
        break
    if item > 150:
        continue 
    if item % 5 == 0:
        print(item)
