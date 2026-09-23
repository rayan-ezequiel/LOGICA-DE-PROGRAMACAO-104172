import os
os.system('cls')

QUANTIDADE = 5
par = 0
impar = 0

for i in range(QUANTIDADE):

    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        par += 1
    else: impar += 1

print(f'A quantidade de pares é: {par}')
print(f'A quantidade de pares é: {impar}')
