import os
os.system('cls')

numeros_totais = []
numeros_pares = []
numeros_impares = []
vez = 1

while True:
    
    numero = float(input(f'Digite o {vez}º número: '))
    numeros_totais.append(numero)
    vez += 1
    
    if numero == 0:
        print('Número invalido.')
        print('Tente digitar um número maior que zero.')
        os.system('cls')
        continue
    
    if numero % 2 == 0.0:
        numeros_pares.append(numero)
    
    else:
        numeros_impares.append(numero)
        continue
    
    if len(numeros_totais) == 6:
        
        print(f'\nNúmeros informados pelo usuário: {numeros_totais}\n')
        print(f'Números pares: {numeros_pares}\n')
        print(f'Números impares: {numeros_impares}\n')
        
        break
