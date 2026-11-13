import os
os.system('cls' if os.name == 'nt' else 'clear')

def logo_senai():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('============')
    print('  SENAI')
    print('============')

def mostrar_dados(nome, idade):
    print(f'{nome} tem {idade} anos.')


logo_senai()

print('\nSOLICITANDO DADOS')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

logo_senai()
print('\nEXIBINDO DADOS')
mostrar_dados(nome, idade)