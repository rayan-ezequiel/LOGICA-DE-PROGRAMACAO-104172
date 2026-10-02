import os
os.system('cls')
import time

print('Cardapio')

print('1 - iPhone Usado: R$ 3.000')
print('2 - Notebook Gamer: R$ 5.500 C/ NF')
print('3 - Monitor 240Hz: R$ 2.200 C/ NF')
print('4 - Placa de Vídeo RTX 4070: R$ 4.800 C/ NF')
print('5 - PC Gamer Completo: R$ 12.000 C/ NF')

um = ('1 - Fone Sem Fio: R$ 300, C/ 1x case, C/ NF')
dois = ('2 - Notebook Gamer: R$ 5.500 C/ NF')
tres = ('3 - Monitor 240Hz: R$ 2.200 C/ NF')
quatro = ('4 - Placa de Vídeo RTX 4070: R$ 4.800 C/ NF')
cinco = ('5 - PC Gamer Completo: R$ 12.000 C/ NF')

escolha = int(input('Qual deseja ? '))

while True:
    match escolha:
        case 1:
            print(f'Você escolheu \n{um}')
        case 2:
            print(f'Você escolheu \n{dois}')
        case 3:
            print(f'Você escolheu \n{tres}')
        case 4:
            print(f'Você escolheu \n{quatro}')
        case 5:
            print(f'Você escolheu \n{cinco}')
    break