import os
os.system('cls' if os.name == 'nt' else 'clear')

# Inversão e Análise de Vetor VETORESINVERSÃO CONDICIONAL
# Preencha uma lista com 6 números inteiros. Gere e imprima uma segunda lista contendo esses mesmos
# elementos na ordem inversa. Ao final, verifique e exiba se a soma de todos os elementos da lista invertida
# resulta em um número par ou ímpa

numeros_inteiros = []
while True:
    try:
        numero = int(input('Digite um número, inteiro.'))
        numeros_inteiros.append()
    except ValueError:
        print('Digite apenas números inteiros.')

    if len(numeros_inteiros) == 6:
        lista_invertida = numeros_inteiros[: : -1]

        if sum(lista_invertida) % 2 == 0:
            print(f'A soma dos elementos da lista invertida, resulta em número par: {sum(lista_invertida)}')
        else:
            print(f'A soma dos elementos da lista invertida, resulta em número impar: {sum(lista_invertida)}')
        soma_das_listas = sum(numeros_inteiros) + sum(lista_invertida)

        if soma_das_listas % 2 == 0:
            print(f'A soma dos elementos das duas listas, resulta em número par: {soma_das_listas}')
        else:
            print(f'A soma dos elementos das duas listas, resulta em número impar: {soma_das_listas}')
        break