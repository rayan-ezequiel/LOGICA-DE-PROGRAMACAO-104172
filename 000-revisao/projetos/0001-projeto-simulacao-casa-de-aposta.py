import os
import random
import time
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

os.system('cls')

saldo = 0

print('Casa de Aposta Rayan ezequiel ')

deposito = int(input('Quanto deseja depositar ? R$ '))
saldo += deposito 
os.system('cls')
print('Bem-vindo a casa de aposta.')

while True:
    
    os.system('cls')
    print(f'Seu saldo é: R$ {saldo}')
    if saldo <= 0:
        print('Seu saldo acabou depoiste para continuar.')
        deposito = int(input('Quanto deseja depositar ? R$ '))
        saldo += deposito
    aposta = int(input('Valor da aposta: R$ '))
    
    if aposta > saldo:
        print('Você não tem saldo suficiente.')
        continue
    elif aposta <= 0:
        print('Você nao pode apostar nada.')
        continue

    saldo -= aposta 
    print('\nGiriando a roleta.')
    time.sleep(1)

    biscoito = '🍪'
    rosca = '🍩'
    chocolate = '🍫'  
    formas = [biscoito, rosca, chocolate]

    escolha = random.choice(formas)
    escolha1 = random.choice(formas)
    escolha2 = random.choice(formas)

    print(f'{escolha} {escolha1} {escolha2}')

    if escolha == escolha1 == escolha2 == chocolate:
            multiplicador = aposta * 2.0
            saldo += multiplicador
            print('Parabéns você ganhou o jogo.')
            print(f'🍫​ 2x. seu saldo agora é: {saldo}')
            
    
    elif escolha == escolha1 == escolha2 == biscoito:
            multiplicador = aposta * 6.0
            saldo += multiplicador
            print('Parabéns você ganhou o jogo.')
            print(f'🍪​ 6x. seu saldo agora é: {saldo}')
            
    
    elif escolha == escolha1 == escolha2 == rosca:
            multiplicador = aposta * 10.0
            saldo += multiplicador
            print('Parabéns você ganhou o jogo.')
            print(f'🍩​ 10x. seu saldo agora é: {saldo}')
            
    else:
        print(f'você perdeu: {saldo}')
         
    jogar_novamente = input('Deseja continuar ? ').lower()
    if jogar_novamente == 'n':
          break
    else: 
          print(f'Vamos continuar!\n')
          continue