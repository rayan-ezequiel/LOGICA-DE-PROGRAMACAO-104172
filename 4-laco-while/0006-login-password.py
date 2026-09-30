import os
import time
os.system('cls')

print('Login e senha.')

#criando conta
print('Criando conta')
for i in range(2):
    while True:
        login = input('Criar login: ')
        senha = input('Criar senha: ')
        break
    print('Login')
    c_login = input('Login: ')
    c_senha = input('Senha: ')
        
    if c_login == login and c_senha == senha:
        print('Suas crendiciais estão certas.')
        break
    else:
        print('senha ou login invalido.')
        time.sleep(2)
        input('pressione. qualquer tecla para continuar...')
        os.system('cls')
        
