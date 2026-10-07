import os
os.system('cls')

numeros_pares = []
numeros_impares = []
soma_pares = 0
soma_impares = 0
soma_geral = 0
quantidade_impares = 0
quantidade_pares = 0

while True:
    valor = float(input('Insira um valor: '))
    if valor == 0:
            break
    elif valor % 2 == 0:
        soma_pares += valor
        quantidade_pares += 1
        
    elif valor % 2 == 1:
        soma_impares += valor
        quantidade_impares + 1

media = soma_pares / quantidade_pares
media_geral = (soma_pares + soma_impares) / (quantidade_pares + quantidade_impares)
print(f'Media dos valores pares: {media}\nMedia Geral: {media_geral}')