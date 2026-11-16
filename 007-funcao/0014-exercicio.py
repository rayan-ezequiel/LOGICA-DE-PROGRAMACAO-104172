import os
os.system('cls' if os.name == 'nt' else 'clear')


def calculo_soma(num1, num2):
    resultado = num1 + num2
    return resultado

def calculo_subtracao(num1, num2):
    resultado = num1 - num2
    return resultado

def calculo_divisao(num1, num2):
    if num2 == 0:
        return 'Atenção esse número não é divisivel por zero...'
    resultado = num1 / num2
    return resultado

def calculo_multi(num1, num2):
    resultado = num1 * num2
    return resultado

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print(f'\nA soma: {calculo_soma(num1, num2)}\n A subtração: {calculo_subtracao(num1, num2)}\n A divisão: {calculo_divisao(num1, num2)}\nA multiplicação: {calculo_multi(num1, num2)}')


