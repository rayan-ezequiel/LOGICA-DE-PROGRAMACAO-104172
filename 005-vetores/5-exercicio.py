import os
import time
os.system('cls')

notas = []

for i in range(3):
    
   
    nota = float(input(f'Digite sua {i + 1}º nota: '))
    notas.append(nota)

print(f'Sua primeira nota foi: {notas[0]}')
print(f'Sua segunda nota foi: {notas[1]}')
print(f'Sua terceira nota foi: {notas[2]}')

