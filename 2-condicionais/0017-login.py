import os
os.system('cls')

while True:
    print('1 - CADASTRO')
    print('2 - lOGIN')
    print('0 - FINALIZAR')

    escolha = input('Escolha uma opção. ')

    if escolha == '1':
        usuario = input('Digite seu usuario: ').lower()
        senha = input('Digite sua senha: ').lower()

        print(f'{usuario} foi cadastrado com sucesso!!')
        print('Bem-Vindo!!!')
    elif escolha == '2':
        print('LOGIN')
        usuariol = input('Digite seu usuario: ').lower()
        senhal = input('Digite sua senha: ').lower()

        if usuariol == usuario and senhal == senha:
            print(f'parabens {usuario}, você foi logado com sucesso.')
            print('Bem-Vindo!!!')
        else: print('Login e senha inválidos!!')
    if escolha == '0':
        print('acabou')
        break





