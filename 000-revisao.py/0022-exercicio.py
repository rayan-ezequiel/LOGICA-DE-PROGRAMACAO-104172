import os
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

candidato_22 = []
canditado_13 = []
canditado_14 = []
invalidos = [] 
nulos = []

while True:
    try:
        voto = int(input('Escolha: '))
    except ValueError:
        print('Inválido.')
        invalidos.append(voto)
    if voto == 22:
        c