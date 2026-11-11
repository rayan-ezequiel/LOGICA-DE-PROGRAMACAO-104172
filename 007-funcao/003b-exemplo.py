import os
os.system('cls')


def cabecalho():
    print('='*15)
    print('    Senai')
    print('='*15)

cabecalho()
nome = input("Digite seu nome: ")

cabecalho()
idade = int(input('Digite sua idade: '))

cabecalho()
print(f'Nome: {nome}')
print(f'Idade: {idade}')
