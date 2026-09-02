import os
import sys
os.system('cls')

print('BANCO MASTER')


#deposito
escolha = input('O que o senhor deseja ? ')
if escolha == 'deposito':
    deposito = input('Quanto o senhor deseja depositar ? ')
    print('Você depositou R$', deposito, 'com sucesso!!')

continuar = "sim"
    while continuar == "sim":
    continuar = input('Deseja fazer outra operação? (sim/nao): ').lower().strip()
#pix
if escolha == 'pix':
    pix = input('Para quem deseja fazer pix ? ').lower
    valor = input('Quanto deseja enviar ? ').lower
    confirmacao = input(f'Você deseja enviar ? {valor} para {pix}').lower
    if confirmacao == 'sim':
        print('transação concluida com sucesso')
    else: print('Ocorreu um erro na transação')
    while continuar == "sim":
    continuar = input('Deseja fazer outra operação? (sim/nao): ').lower().strip()
#saque
if escolha == 'saque':
    saldo = print('sua conta tem: ', deposito)
    saque = input('Quanto o senhor deseja sacar ? ')
    print(f'você sacou {saque} parabens')

    


    # COLOQUE TODO O SEU CÓDIGO AQUI (Menu, Depósito, Pix, Saque...)
    # Lembre-se de dar 4 espaços para a direita em todas as linhas do seu código!
    
    # Esta deve ser a última linha de dentro do while:





    



    
