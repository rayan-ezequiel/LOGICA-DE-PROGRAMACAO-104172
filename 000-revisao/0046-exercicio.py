import os 
import time
import sys

os.system('cls' if os.name == 'nt' else 'clear')

senha_certa = '123'
depositos = []
saques = []
def senha_de_acesso():
    erros_senha = 0
    for tentativas in range(3):
        print('== SENHA DE ACESSO ==')
        senha_de_acesso = input('Digite sua senha: ')
        if senha_de_acesso == senha_certa:
            print('ACESSO AUTORIZADO')
            break
        else:
            print(f'ACESSO RECUSADO Restam {2 - tentativas} tentativas.\n')
        if senha_de_acesso != senha_certa:
            erros_senha += 1
            if erros_senha == 3:
                print('Número de tentativas atingido.\nCONTA BLOQUEADA')
                sys.exit()
    time.sleep(0.7)

def menu():
    print('=== BANCO COFRINHO · CAIXA ===')
    print('1 - Ver saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Ver extrato')
    print('0 - Sair')

def ver_saldo():
    print(f'Seu saldo é de: R$ {saldo:.2f}')
    time.sleep(0.7)

def deposito(saldo):
    
    print('== DEPOSITO ==')
    try:
        depositar = float(input('Valor do depósito: '))
        if depositar <= 0:
            print('ERROR: Valor menor ou igual a zero...')
            return saldo
        depositos.append(depositar)
        saldo += depositar
    except ValueError:
        print('Valor inválido')
    return saldo

        

def saque(saldo):
    print('== SAQUE ==')
    try:
        sacar = float(input('Valor do saque: '))
        if sacar > 1000:
            print('LIMITE DE R$ 1000 EXCEDIDO')
        elif sacar <= 0:
            print('ERROR: Valor inválido...')
        elif sacar > saldo:
            print('ERROR: Saldo insuficiente...')
        else:
            print('SAQUE FEITO COM SUCESSO')
            saques.append(sacar)
            saldo -= sacar
    except ValueError:
        print('Valor inválido')
    return saldo

def ver_extrato(depositos, saques):    
    print('== EXTRATO BANCÁRIO ==')
    print(f'\n== DEPÓSITOS ({len(depositos)}) ==')
    if not depositos:
        print('Depositos\nNenhuma movimentação.')
    for d in depositos:
        print(f'+ {d:.2f}')
    
    print(f'\n== SAQUES ({len(saques)}) ==')
    if not saques:
        print('Saques\nNenhuma movimentação.')
    for s in saques:
        print(f'- {s:.2f}')
    print(f'\nSALDO: {saldo:.2f}')

saldo = 500.0

senha_de_acesso()

while True:
    menu()
    escolha = int(input('\nEscolha uma opção: '))
    match escolha:
        case 1:
            ver_saldo()
        case 2:
            saldo = deposito(saldo)
        case 3:
            saldo = saque(saldo)
        case 4:
            ver_extrato(depositos, saques)
        case 0:
            print('Obrigado por usar o programa !')
            sys.exit()
        case _:
            print('Opção inválida.')