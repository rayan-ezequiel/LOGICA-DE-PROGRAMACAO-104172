#Objetivo: Peça para o usuário digitar um valor em Reais (R$) e mostre quanto esse valor seria em Dólares (US$).

import os
os.system('cls')

print('= Conversor de Moedas =')

real = float(input('Digite o valor R$: '))

print('O valor do Dolar é: ',(real / 5.14))

print('= Dolar para real =')

dolar = float(input('Digite o valor do Dolar: '))

print('O valor em reais é: ', (dolar * 5.14))




