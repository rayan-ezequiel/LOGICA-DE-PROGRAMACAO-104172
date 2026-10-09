import os
os.system('cls')

# Faça um programa que leia um nome de usuário e a 
# sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome_de_usuario = input('Digite seu nome de usuario: ').lower()
    senha = input('Digite sua senha: ').lower()
    if senha == nome_de_usuario:
        os.system('cls')
        print('nome de usuario e senha são os mesmos\ntente novamente...')
        continue
    else: print('parabéns, logado com sucesso...')
    break

