import os
os.system('cls')

numero1 = float(input('Digite o primeiro numero: '))
operador = input('Digite o operador soma(+), produto(*), divisão(/), subtração(-), potência(**): ')
numero2 = float(input('Digite o segundo numero: '))

if operador == '-': 
    print('O resultado é: ', numero1 - numero2)
elif operador == '+':
    print('O resultado é: ', numero1 + numero2)
elif operador == '/':
    print('O resultado é: ', numero1 / numero2)
elif operador == '*':
    print('O resultado é: ', numero1 * numero2)
elif operador == '**':
    print('O resultado é: ', numero1 ** numero2)

