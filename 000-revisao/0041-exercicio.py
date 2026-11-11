import os
os.system('cls')

while True:
    nota = int(input('Digite sua nota entre 1 e 10: '))
    if nota <= 10 and nota >= 0:
    #outro jeito: if 0 <= nota =< 10:
        print(f'Sua nota é {nota}')
        break
    else: print('nota invalida tente novamente...')