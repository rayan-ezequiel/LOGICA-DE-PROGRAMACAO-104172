import os
os.system('cls')

def mostrar_saudacao(nome, idade):
    print(f'{nome} tem {idade} anos.')

print('= Solicitando Dados =')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

print('\n= Exibindo Dados =')
mostrar_saudacao(nome, idade)