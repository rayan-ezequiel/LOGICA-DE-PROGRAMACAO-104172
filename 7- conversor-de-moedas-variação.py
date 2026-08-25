#Objetivo: Peça para o usuário digitar um valor em Reais (R$) e mostre quanto esse valor seria em Dólares (US$).

import os
os.system('cls')

print('= Conversor de Moedas =')

valor_em_reais = float(input('Digite o valor em reais: '))
calculo_para_dolar = float(valor_em_reais / 5.14)

print('= Resultado =')
print('O valor convertido para dolar é: ' '$', calculo_para_dolar)
print('O valor original: ' 'R$',valor_em_reais)






