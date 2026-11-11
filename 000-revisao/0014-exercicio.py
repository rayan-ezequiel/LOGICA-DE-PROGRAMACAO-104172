import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')

rodando = True

while rodando:
    
    print('\nMenu interativos com Operações')
    print('\n[1] Tabuada de um número\n[2] Somar de 1 até N\n[3] Sair')
    escolha = int(input('Escolha: '))
    
    if escolha == 1:
        
        numero = float(input('Digite um número: '))
        
        for i in range(1, 11):
            print(f'{numero} x {i} = {numero * i}')
    
    elif escolha == 2:
        
        numero = int(input('Digite um número: '))
        
        for i in range(1, numero + 1):
            print(f'{i} + {numero} = {i + numero}')

    elif escolha == 3:
        
        while True:

            try:
                confirmacao = int(input('Realmente deseja sair ?\n[1] Para sim\n[2] Para não\nEscolha: '))
            
            except ValueError:
                print('ERROR: Digite um número inteiro.')
            
            if confirmacao == 1:
                print('Até a proxima.')
                sys.exit()
            
            elif confirmacao == 2:
                print('Voltando ao programa.')
                break
            
            else:
                print('opcão inválida.\nTente novamente.')
                continue
