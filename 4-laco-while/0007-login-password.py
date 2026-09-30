import os
os.system('cls')
clogin = 'Rayan'
csenha = 'senha123'

while True:
    for i in range(3):
        login = input('Digite seu login: ')
        senha = input('Digite seu login: ')

        if login == clogin and csenha == senha:
            print('Bem vindo')
        else: print('Senha invalida.')

