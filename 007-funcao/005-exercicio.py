import os
os.system('cls')

def logo_senai():
    os.system('cls')
    print('='*15)
    print(' SENAI - BAHIA')
    print('='*15)
def mostrar_dados(nome, email, telefone):
    print(f'Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}')


logo_senai()
nome = input('Digite seu nome: ')
logo_senai()
email = input('Digite seu e-mail: ')
logo_senai()
telefone = int(input('Digite seu telefone: '))
print('= SOLICITANDO OS DADOS =')
mostrar_dados(nome, email, telefone)