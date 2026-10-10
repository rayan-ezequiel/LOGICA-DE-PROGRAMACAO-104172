import os
os.system('cls')

numeros = []

while True:
    
    numero = float(input('Digite um número: '))
    numeros.append(numero)
    
    if len(numeros) == 5:
        os.system('cls')
        
        print(f'\nO maior número é: {max(numeros)}\n')
        print(f'O menor número é: {min(numeros)}\n')
        print(f'Os números infomrados pelo usuario foram {numeros}\n')
        
        break