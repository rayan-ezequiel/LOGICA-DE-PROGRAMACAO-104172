import os
os.system('cls' if os.name == 'nt' else 'clear')

# Validação de Senha com Tentativas Limite WHILE CONTADOR SEGURANÇA
# Crie um sistema de login simples que peça uma senha numérica. Dê ao usuário no máximo 3 tentativas para
# acertar a senha (ex: 1234). Se acertar, exiba "Acesso concedido" e encerre; se errar todas as 3 vezes, imprima
# "Conta bloqueada".

print('Validação de Senha com Tentativas Limite')
tentativas = 0
while True:
    
    if tentativas == 3:
        print('Acesso Bloqueado.')
        break
    
    else:
        # CADASTRO
        try:
            usuario = 'USUARIO: usuario001'
            senha = int(input('Senha: Digite sua senha numerica: '))
        except ValueError:
            print('Digite apenas números inteiros.')
            
        # LOGIN
        print('Tela de login')
        print('USUARIO: usuario001')
        
        try:
            senha_login = int(input('Digite a senha criada: '))
        
        except ValueError:
            print('Digite apenas números inteiros.')
            tentativas += 1
            

        if senha == senha_login:
            print('Acesso concedido.')
            break
        
        elif senha != senha_login:        
            print('Senha errada.')
            tentativas += 1
            continue
        
        else:
            print('Enrada inválida, tente novamente.')
            tentativas += 1
            continue

        



