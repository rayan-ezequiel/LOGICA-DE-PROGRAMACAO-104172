import os
import time
os.system('cls')

print('Login e senha.')
login = input('Criar login: ')
senha = input('Criar senha: ')
os.system('cls')

print('Criando conta')

while True:
    print('Login')
    c_login = input('Login: ')
    c_senha = input('Senha: ')
    if c_login == login and c_senha == senha:
        print('Suas crendiciais estão certas.')
        break
    else:
        print('senha ou login invalido.')
        input('pressione. qualquer tecla para continuar...')
        time.sleep(1)
        os.system('cls')
