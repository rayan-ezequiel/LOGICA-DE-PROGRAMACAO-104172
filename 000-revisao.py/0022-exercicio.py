import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

# Sistema de Urna Eletrônica WHILE CONTADORES ELEIÇÃO
# Crie um programa de votação com 3 candidatos (opções 1, 2 e 3). Receba votos até que seja digitado 0. Ao
# final, exiba o total de votos de cada candidato, a quantidade de votos nulos/inválidos e identifique o candidato
# vencedor.


print('Sistema de Urna Eletrônica')
print('22 - Flávio Bolsonaro')
print('13 - Lula')
print('14 - Renan Santos')
print('0 - Sair')


candidato_22 = 0
canditado_13 = 0
canditado_14 = 0
invalidos = 0
nulos = 0



vez = 0
while True:
    vez += 1
    try:
        voto = int(input('Escolha: '))
        if voto == 22:
            confirmar = input('Confirma voto em Flávio Bolsonaro? (S/N): ').upper()
            if confirmar == 'S':
                candidato_22 += 1
                print('voto confirmado com sucesso')
        elif voto == 13:
            confirmar = input('Confirma voto em Lula? (S/N): ').upper()
            if confirmar == 'S':
                canditado_13 += 1
                print('Você nao votou consciente...')
        elif voto == 14:
                confirmar = input('Confirma voto em Renan Santos? (S/N): ').upper()
                if confirmar == 'S':
                    candidato_14 += 1
                    print('voto confirmado com sucesso')
        else:
            print('Candidato inválido...')
            invalidos += 1
    except ValueError:
        print('Inválido.')
        invalidos += 1
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

    if vez == 10:
        break
print('RESULTADO DAS ELEIÇÕES')

print(f'VENCEDOR: {max(candidato_22, canditado_13, canditado_13) }')
print(f'ULTIMO: {min(candidato_22, canditado_13, canditado_13)}')
print(f'NULOS/INVÁLIDOS: {invalidos}')
        
    