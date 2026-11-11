import os
os.system('cls')

print('+ SOLICITANDO DADOS +')
def tabuada(i):
    for i in range(11):
        print(f'{numero} x {i} = {numero * i}')
print('+ RESULTADO +')
numero = int(input('Digite um número: '))
tabuada(numero)