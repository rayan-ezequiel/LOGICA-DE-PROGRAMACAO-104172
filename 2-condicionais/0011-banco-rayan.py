import os
os.system('cls')

print('BANCO RAYAN')

saldo = 0 
continuar = True

while continuar:
    
    escolha = input('BEM VINDO AO BANCO RAYAN !!!\nO que você deseja fazer ? ').lower()

    if escolha == 'deposito': 
        deposito = float(input('Quanto deseja depositar? '))
        saldo += deposito
        print(f'Você depositou R${deposito}\nSaldo atual: R${saldo}.')

    elif escolha == 'pix':

        nome = input('Para quem deseja envia ? ')
        valor = float(input(f'Quanto deseja enviar para {nome} ?' ))

        if valor > saldo:
            print('Você nao tem dinheiro suficiente para essa transação.')
        elif valor <= saldo:
            saldo -= valor
            confirmar = input(f'Você deseja enviar {nome}, o valor de {valor} ?' ).lower()
            if confirmar == 'sim':
                print('Transação concluida com sucesso')
                
    elif escolha == 'saque':
        saque = float(input('Quanto deseja sacar  ? '))

        if saque > saldo:
            print(f'Você nao pode sacar R${saque}, pois não tem saldo suficente.')

        elif saque <= saldo: 
            saldo -= saque
            print(f'Você sacou R${saque}, seu saldo agora é: R${saldo}.')

    elif escolha == 'saldo':
        print(f'Seu saldo é {saldo}.')
    else: print('opcção invalida.')

    saida = input('Deseja sair ? ').lower()
    if saida == 'sim': 
        continuar = False