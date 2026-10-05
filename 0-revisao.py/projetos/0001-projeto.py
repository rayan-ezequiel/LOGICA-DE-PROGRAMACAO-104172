import os
import random
import time
os.system('cls')

print('Casa de Aposta Rayan ezequiel ')

saldo = 0
for i in range(3):
    while True:
        deposito = int(input('Quanto deseja depositar ? '))
        saldo += deposito
        print('Bem-vindo a casa de aposta.')
        print('Quanto deseja apostar ? ')
        
        aposta = int(input('Escolha: '))
        
        if aposta > 0:
            print('Vamos começar: ')
            
            formas = ['​🍪​', '🍩', '🍫​']
            
            escolha = random.choice(formas)
            escolha1 = random.choice(formas)
            escolha2 = random.choice(formas)
            
            print(escolha, escolha1, escolha2)
            
            if (escolha, escolha1, escolha2) == '🍫​':
                multi = aposta * 2.0
                saldo += multi
                print('Parabéns você ganhou o jogo.')
                print(f'🍫​ 2x. seu saldo agora é: {saldo}')
            
            elif (escolha, escolha1, escolha2) == '🍪​':
                multi = aposta * 6.0
                saldo += multi
                print('Parabéns você ganhou o jogo.')
                print(f'🍪​ 6x. seu saldo agora é: {saldo}')
            
            elif (escolha, escolha1, escolha2) == '🍩​':
                multi = aposta * 10.0
                saldo += multi
                
                print('Parabéns você ganhou o jogo.')
                print(f'🍩​ 10x. seu saldo agora é: {saldo}')
            else:
                saldo -= aposta
                print(f'Você perdeu seu saldo agora é: {saldo}')
                continue
        break
    break

