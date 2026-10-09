import os
os.system('cls')

while True:
    numero = int(input('Digite um numero entre 1 e 10: '))
    if numero < 1 or numero > 10:
        print('Número invalido, tente novamente!')
    else:
        print('O número está entre 1 a 10.')
        break #Serve para quebrar o loop.
print ('fim')