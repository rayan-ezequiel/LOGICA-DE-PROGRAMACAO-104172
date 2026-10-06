import os
import random
import time
import sys
# Força a saída padrão do terminal a aceitar emojis e caracteres especiais
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

os.system('cls')

saldo = 0

print('Casa de Aposta Rayan ezequiel ')

#deposito esta fora do loop, pois voce precisa começar depositando dinheiro. caso ao contrario, nao
#tera como jogar
deposito = int(input('Quanto deseja depositar ? '))
saldo += deposito 

print('Bem-vindo a casa de aposta.')
while True:
    
    print(f'Seu saldo é: {saldo}')
    if saldo <= 0:
        print('Seu saldo acabou depoiste para continuar.')
        deposito = int(input('Quanto deseja depositar ? '))
        os.system('cls')
        saldo += deposito
    aposta = int(input('Valor da aposta: '))
    
    # validação da aposta 
    if aposta > saldo:
        print('Você não tem saldo suficiente.')
        continue
    elif aposta <= 0:
        print('Você nao pode apostar nada.')
        continue

    saldo -= aposta 
    print('\nGiriando a roleta.')
    time.sleep(1)


    #conteudo que vai ter nos slots, sendo armazenando na lista 'formas'.
    biscoito = '🍪'
    rosca = '🍩'
    chocolate = '🍫'  
    formas = [biscoito, rosca, chocolate]

    #definindo a aleatoriedade dos 3 slots.
    escolha = random.choice(formas)
    escolha1 = random.choice(formas)
    escolha2 = random.choice(formas)

    print(f'{escolha} {escolha1} {escolha2}')


    # esses ifs e elifs servem para mostrar como o codigo vai comportar a cada vitoria.
    if escolha == escolha1 == escolha2 == chocolate:
            multiplicador = aposta * 2.0
            saldo += multiplicador
            print('Parabéns você ganhou o jogo.')
            print(f'🍫​ 2x. seu saldo agora é: {saldo}')
            os.system('cls')
    
    elif escolha == escolha1 == escolha2 == biscoito:
            multiplicador = aposta * 6.0
            saldo += multiplicador
            print('Parabéns você ganhou o jogo.')
            print(f'🍪​ 6x. seu saldo agora é: {saldo}')
            os.system('cls')
    
    elif escolha == escolha1 == escolha2 == rosca:
            multiplicador = aposta * 10.0
            saldo += multiplicador
            print('Parabéns você ganhou o jogo.')
            print(f'🍩​ 10x. seu saldo agora é: {saldo}')
            os.system('cls')
    else:
        print(f'você perdeu: {saldo}')
        continue
    
    
    # Esse comentário serve para fazer o jogo coninuar se voce quiser ou nao 
    jogar_novamente = input('Deseja continuar ? ').lower()
    if jogar_novamente == 'n':
          break
    else: 
          print(f'Vamos continuar!\nSaldo{saldo}')
          continue
    
    

