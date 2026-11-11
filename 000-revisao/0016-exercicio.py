import os
os.system('cls' if os.name == 'nt' else 'clear')

numeros_pares = []
numeros_impares = []

for i in range(10):
    numero = float(input(f'Digite seu {i + 1}º número: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(f'Números pares: {numeros_pares}\nNUmeros impares: {numeros_impares}\nQuantidade de elementos: ')
print(f'Pares: {len(numeros_pares)}\nImpares: {len(numeros_impares)}')