import random
import os
os.system('cls')

ferramentas = random.choice(('pedra', 'papel','tesoura'))
escolha = input('Digite sua escolha: ')

#vitorias
if escolha == 'tesoura' and ferramentas == 'papel':
    print('maquina escolheu ',ferramentas, 'você ganhou!!')

elif escolha == 'papel' and ferramentas == 'tesoura':
    print('maquina escolheu',ferramentas, 'você perdeu!!')
#vitorias
if escolha == 'pedra' and ferramentas == 'tesoura':
    print('maquina escolheu',ferramentas, 'você ganhou!!')
elif escolha == 'tesoura' and ferramentas == 'pedra':
    print('maquina escolheu ',ferramentas, 'você perdeu!!')
#vitorias

if escolha == 'papel' and ferramentas == 'pedra':
    print('maquina escolheu',ferramentas, 'você ganhou!!')
elif escolha == 'pedra' and ferramentas == 'papel':
    print('maquina escolheu',ferramentas, 'você perdeu!!')








