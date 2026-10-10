import os
os.system('cls')

# Crie um algoritmo que receba do usuário valores e 
# armazene em um vetor 5 números, caso seja informado um valor negativo, 
# atribua o valor 0.

# - Liste os valores do vetor.

numeros_positivos = []

while True:
    positivos = (int(input(f'Digite um número: ')))
    
    if positivos < 0:
        numeros_positivos.append(0)
    else: 
         numeros_positivos.append(positivos)
    
    if len(numeros_positivos) == 5:
            print(numeros_positivos)
            break
