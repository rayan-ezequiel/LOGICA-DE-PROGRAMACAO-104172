import os
os.system('cls')

print('Nota 0 a 10')

nota = float(input('Digite sua nota: '))

if nota <= 10 and nota >= 0:
    print(nota)
else: print('a nota deve ser entre 0 a 10.')