import os
os.system('cls' if os.name == 'nt' else 'clear')
def numero_impar_ou_par(numero):
    if numero % 2 == 0:
        return 'O número é par'
    else:
        return 'o número é impar'
numero = int(input('Digite um número: '))

resultado = numero_impar_ou_par(numero)

print(resultado)