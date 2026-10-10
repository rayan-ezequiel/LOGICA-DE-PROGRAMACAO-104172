import os
os.system('cls')

numeros_totais = []
numeros_pares = []
numeros_impares = []

while True:
    
    numero = float(input('Digite um número: '))
    numeros_totais.append(numero)
    
    if len(numeros_totais) == 6:
            print(f'\nNúmeros informados pelo usuário: {numeros_totais}\n')
            print(f'Números pares: {numeros_pares}\n')
            print(f'Números impares: {numeros_impares}\n')
            break
    else:
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else: 
            numeros_impares.append(numero)
    
    
    
